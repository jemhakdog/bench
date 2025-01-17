import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import html2text
import time
from collections import deque
import argparse
from typing import Optional, List, Set
import sys
import logging
from datetime import datetime
import concurrent.futures
from threading import Lock
from queue import Queue

class DocsIndexer:
    """A web scraper that indexes documentation pages and saves them as markdown."""
    
    def __init__(self, base_url: str, delay: float = 1.0, max_pages: Optional[int] = None, num_workers: int = 4):
        """
        Initialize the docs indexer.
        
        Args:
            base_url: The starting URL to begin scraping from
            delay: Time to wait between requests in seconds
            max_pages: Maximum number of pages to scrape (None for unlimited)
            num_workers: Number of concurrent workers
        """
        self.base_url = base_url
        self.base_domain = urlparse(base_url).netloc
        self.visited_urls: Set[str] = set()
        self.url_queue: Queue = Queue()
        self.url_queue.put(base_url)
        self.content: List[str] = []
        self.delay = delay
        self.max_pages = max_pages
        self.num_workers = num_workers
        
        # Thread safety
        self.visited_lock = Lock()
        self.content_lock = Lock()
        self.pages_scraped = 0
        self.pages_lock = Lock()
        
        # Configure HTML to Markdown converter
        self.h = html2text.HTML2Text()
        self.h.ignore_links = False
        self.body_width = 0
        
        # Setup session with headers
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 Documentation Indexer Bot (respectful scraping)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
        })
        
    def is_same_domain(self, url: str) -> bool:
        """Check if URL belongs to same domain"""
        return urlparse(url).netloc == self.base_domain
    
    def normalize_url(self, url: str) -> str:
        """Normalize URL to prevent duplicates"""
        parsed = urlparse(url)
        # Remove fragments
        return parsed._replace(fragment='').geturl()
    
    def get_links(self, soup: BeautifulSoup, current_url: str) -> List[str]:
        """Extract and normalize all links from page"""
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            absolute_url = urljoin(current_url, href)
            normalized_url = self.normalize_url(absolute_url)
            if self.is_same_domain(normalized_url):
                links.append(normalized_url)
        return links
    
    def extract_content(self, soup: BeautifulSoup, url: str) -> str:
        """Extract main content from page"""
        # Try to find main content area
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content')
        
        if main_content:
            content = main_content
        else:
            # Fallback to body if no main content area found
            content = soup.find('body')
            
        # Convert to markdown
        markdown = self.h.handle(str(content))
        
        # Add URL as header
        return f"# {url}\n\n{markdown}\n\n---\n\n"
    
    def worker(self) -> None:
        """Worker function for concurrent scraping"""
        while True:
            # Check if we've reached max pages
            with self.pages_lock:
                if self.max_pages and self.pages_scraped >= self.max_pages:
                    break
            
            try:
                # Get next URL with timeout
                current_url = self.url_queue.get(timeout=1)
            except:
                # Queue is empty
                break
                
            # Skip if already visited
            with self.visited_lock:
                if current_url in self.visited_urls:
                    self.url_queue.task_done()
                    continue
                self.visited_urls.add(current_url)
            
            try:
                # Add delay to be nice to servers
                time.sleep(self.delay)
                
                logging.info(f"Scraping: {current_url}")
                
                response = self.session.get(current_url)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract content
                content = self.extract_content(soup, current_url)
                with self.content_lock:
                    self.content.append(content)
                
                # Get links and add to queue
                links = self.get_links(soup, current_url)
                new_links = 0
                for link in links:
                    with self.visited_lock:
                        if link not in self.visited_urls:
                            self.url_queue.put(link)
                            new_links += 1
                
                with self.pages_lock:
                    self.pages_scraped += 1
                    pages = self.pages_scraped
                
                logging.info(f"✓ Found {new_links} new links | Queue size: {self.url_queue.qsize()} | Total scraped: {pages}")
                
            except requests.exceptions.RequestException as e:
                logging.error(f"⚠ Network error scraping {current_url}: {e}")
            except Exception as e:
                logging.error(f"⚠ Error scraping {current_url}: {e}")
            finally:
                self.url_queue.task_done()
    
    def scrape(self) -> None:
        """Main scraping function using thread pool"""
        logging.info(f"Starting scrape from {self.base_url} with {self.num_workers} workers")
        logging.info(f"Rate limiting: {self.delay} seconds between requests")
        if self.max_pages:
            logging.info(f"Will scrape up to {self.max_pages} pages")
        
        # Create thread pool
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            # Start workers
            futures = []
            for _ in range(self.num_workers):
                futures.append(executor.submit(self.worker))
            
            # Wait for all workers to complete
            try:
                concurrent.futures.wait(futures)
            except KeyboardInterrupt:
                logging.warning("\nScraping interrupted by user. Waiting for workers to finish...")
                executor.shutdown(wait=True)
        
        logging.info(f"\nScraping complete! Processed {self.pages_scraped} pages")
    
    def save_content(self, filename: str) -> None:
        """Save all content to markdown file"""
        if not self.content:
            logging.warning("No content to save!")
            return
            
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(''.join(self.content))
            logging.info(f"Successfully saved content to {filename}")
        except Exception as e:
            logging.error(f"Error saving to {filename}: {str(e)}")

def setup_logging(log_file=None):
    """Setup logging configuration"""
    if log_file is None:
        log_file = f"scraper_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return log_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape documentation and save as markdown')
    parser.add_argument('url', help='The base URL to start scraping from')
    parser.add_argument('--output', '-o', default='docs.md', help='Output markdown file (default: docs.md)')
    parser.add_argument('--delay', '-d', type=float, default=1.0, help='Seconds to wait between requests (default: 1.0)')
    parser.add_argument('--max-pages', '-m', type=int, help='Maximum number of pages to scrape')
    parser.add_argument('--workers', '-w', type=int, default=4, help='Number of concurrent workers (default: 4)')
    parser.add_argument('--log-file', help='Log file path (default: auto-generated)')
    
    args = parser.parse_args()
    
    # Setup logging
    log_file = setup_logging(args.log_file)
    
    indexer = DocsIndexer(args.url, delay=args.delay, max_pages=args.max_pages, num_workers=args.workers)
    indexer.scrape()
    indexer.save_content(args.output)
    
    logging.info(f"Done! Documentation saved to {args.output}")
    logging.info(f"Full logs available in: {log_file}")
