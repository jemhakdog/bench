from typing import List

class Page:
    def __init__(self):
        self.current_page = 1
    def set_current_page(self, current_page):
        self.current_page = current_page
    def get_current_page(self):
        return self.current_page
    
class Filters:
    def __init__(self):
        self.filters = []
    def set_current_filters(self, filters):
        self.filters = filters
    def get_current_filters(self):
        return self.filters

class TotalPages:
    def __init__(self):
        self.total_pages = 0
    def set_total_pages(self, total_pages):
        self.total_pages = total_pages
    def get_total_pages(self):
        return self.total_pages

class Pagination:
    def __init__(self, page: Page, total_pages: TotalPages, filters: Filters):
        self._page = page
        self._total_pages = total_pages
        self._filters = filters

    def get_page(self) -> Page:
        return self._page

    def set_page(self, page: Page):
        self._page = page

    def get_total_pages(self) -> TotalPages:
        return self._total_pages

    def set_total_pages(self, total_pages: TotalPages):
        self._total_pages = total_pages

    def get_filters(self) -> Filters:
        return self._filters

    def set_filters(self, filters: Filters):
        self._filters = filters

def generate_pagination_links(current_page: int, total_pages: int) -> str:
    """
    Generate HTML pagination links.
    
    Args:
        current_page (int): The current page number
        total_pages (int): The total number of pages
        
    Returns:
        str: HTML string containing pagination links
    """
    pagination_links = ""
    print("generate_pagination_links:", current_page, total_pages)

    start_page = max(1, current_page - (5 // 2))
    end_page = min(total_pages, start_page + 5 - 1)
    # Adjust start_page if at the end of range
    if end_page - start_page < 5 - 1:
        start_page = max(1, end_page - 5 + 1)

    # Previous button
    if current_page > 1:
        pagination_links += f"<li class='page-item'><a class='page-link' href='?page={current_page - 1}'>Previous</a></li>"

    # Page links
    for p in range(start_page, end_page + 1):
        if p == current_page:
            pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
        else:
            pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"

    # Next button
    if current_page < total_pages:
        pagination_links += f"<li class='page-item'><a class='page-link' href='?page={current_page + 1}'>Next</a></li>"

    # Current page of total pages
    pagination_links += f"<li class='page-item disabled'><span class='page-link'>Page {current_page} of {total_pages}</span></li>"
    
    # Jump to page select
    pagination_links += f"""
        <li class='page-item'>
        <select class='page-link form-select' aria-label='Jump to' onchange='window.location.href = "?page=" + (this.value === "jump to" ? 1 : this.value)' >
            <option value='1' selected>jump to</option>
                {"".join(f"<option value='{p}' {'selected' if p == current_page else ''}>{p}</option>" for p in range(1, total_pages + 1))}
            </select>
        </li>
    """
    return pagination_links

# Initialize global pagination objects
current_page = Page()
filterz = Filters()
total_pagez = TotalPages()
pagination = Pagination(None, None, None)