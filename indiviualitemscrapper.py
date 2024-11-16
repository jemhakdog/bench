import requests
from bs4 import BeautifulSoup
import json
import html

class ProductExtractor:
    def __init__(self, url):
        self.url = url
        self.product_data = {}
        self.other_colors_data = {}

    def fetch_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")

    def extract_product_data(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract the JSON-LD script
        json_ld_script = soup.find('script', type='application/ld+json')
        if json_ld_script:
            json_ld_data = json_ld_script.string
            self.product_data = json.loads(json_ld_data)
        else:
            raise Exception("No JSON-LD script found.")

    # def decode_other_colors_from_html(self, html_content):
    #     soup = BeautifulSoup(html_content, 'html.parser')
        
    #     # Find the <ul> element with the class 'other-colors-items'
    #     other_colors_ul = soup.find('ul', class_='other-colors-items')
        
    #     if other_colors_ul:
    #         # Get the data-mage-init attribute
    #         data_mage_init = other_colors_ul.get('data-mage-init')
            
    #         if data_mage_init:
    #             # Extract the JSON string from the data-mage-init attribute
    #             start_index = data_mage_init.find('{"other-colors":')
    #             end_index = data_mage_init.rfind('}}') + 2  # Include the closing braces
    #             json_string = data_mage_init[start_index:end_index]
                
    #             # Unescape the JSON string
    #             unescaped_json_string = html.unescape(json_string)
                
    #             # Load the JSON data into a Python dictionary
    #             try:
    #                 self.other_colors_data = json.loads(unescaped_json_string)
                    
    #                 # Parse the products string into a JSON object
    #                 if 'other-colors' in self.other_colors_data and 'products' in self.other_colors_data['other-colors']:
    #                     products_string = self.other_colors_data['other-colors']['products']
    #                     products = json.loads(products_string)  # Parse the products string
    #                     self.other_colors_data['other-colors']['products'] = products  # Update the product data
    #             except json.JSONDecodeError as e:
    #                 raise Exception("Error decoding JSON: " + str(e))
    #         else:
    #             raise Exception("No data-mage-init attribute found.")
    #     else:
    #         raise Exception("No <ul> element with class 'other-colors-items' found.")


    def decode_other_colors_from_html(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the <ul> element with the class 'other-colors-items'
        other_colors_ul = soup.find('ul', class_='other-colors-items')
        
        if other_colors_ul:
            # Get the data-mage-init attribute
            data_mage_init = other_colors_ul.get('data-mage-init')
            
            if data_mage_init:
                # Extract the JSON string from the data-mage-init attribute
                start_index = data_mage_init.find('{"other-colors":')
                end_index = data_mage_init.rfind('}}') + 2  # Include the closing braces
                
                if start_index == -1 or end_index == -1:
                    print("Warning: JSON structure not found in data-mage-init attribute.")
                    return  # Early return if the JSON structure is not found
                
                json_string = data_mage_init[start_index:end_index]
                
                # Unescape the JSON string
                unescaped_json_string = html.unescape(json_string)
                
                # Load the JSON data into a Python dictionary
                try:
                    self.other_colors_data = json.loads(unescaped_json_string)
                    
                    # Parse the products string into a JSON object
                    if 'other-colors' in self.other_colors_data and 'products' in self.other_colors_data['other-colors']:
                        products_string = self.other_colors_data['other-colors']['products']
                        products = json.loads(products_string)  # Parse the products string
                        self.other_colors_data['other-colors']['products'] = products  # Update the product data
                    else:
                        print("Warning: 'other-colors' or 'products' not found in the JSON data.")
                except json.JSONDecodeError as e:
                    print("Error decoding JSON: " + str(e))
            else:
                print("Warning: No data-mage-init attribute found.")
        else:
            print("Warning: No <ul> element with class 'other-colors-items' found.")
    def extract_data(self):
        html_content = self.fetch_page()
        self.extract_product_data(html_content)
        self.decode_other_colors_from_html(html_content)

        result = []
        if self.product_data:  # Check if product_data has a value
            result.append(self.product_data)
        if self.other_colors_data:  # Check if other_colors_data has a value
            result.append(self.other_colors_data)

        return result
# Usage


import requests
from bs4 import BeautifulSoup
import json
import html

class ProductExtractor:
    def __init__(self, url):
        self.url = url
        self.product_data = {}
        self.other_colors_data = {}
        self.magento_data = {}

    def fetch_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")

    def extract_product_data(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract the JSON-LD script
        json_ld_script = soup.find('script', type='application/ld+json')
        if json_ld_script:
            json_ld_data = json_ld_script.string
            self.product_data = json.loads(json_ld_data)
        else:
            raise Exception("No JSON-LD script found.")

    def decode_other_colors_from_html(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the <ul> element with the class 'other-colors-items'
        other_colors_ul = soup.find('ul', class_='other-colors-items')
        
        if other_colors_ul:
            # Get the data-mage-init attribute
            data_mage_init = other_colors_ul.get('data-mage-init')
            
            if data_mage_init:
                # Extract the JSON string from the data-mage-init attribute
                start_index = data_mage_init.find('{"other-colors":')
                end_index = data_mage_init.rfind('}}') + 2  # Include the closing braces
                
                if start_index == -1 or end_index == -1:
                    print("Warning: JSON structure not found in data-mage-init attribute.")
                    return  # Early return if the JSON structure is not found
                
                json_string = data_mage_init[start_index:end_index]
                
                # Unescape the JSON string
                unescaped_json_string = html.unescape(json_string)
                
                # Load the JSON data into a Python dictionary
                try:
                    self.other_colors_data = json.loads(unescaped_json_string)
                    
                    # Parse the products string into a JSON object
                    if 'other-colors' in self.other_colors_data and 'products' in self.other_colors_data['other-colors']:
                        products_string = self.other_colors_data['other-colors']['products']
                        products = json.loads(products_string)  # Parse the products string
                        self.other_colors_data['other-colors']['products'] = products  # Update the product data
                    else:
                        print("Warning: 'other-colors' or 'products' not found in the JSON data.")
                except json.JSONDecodeError as e:
                    print("Error decoding JSON: " + str(e))
            else:
                print("Warning: No data-mage-init attribute found.")
        else:
            print("Warning: No <ul> element with class 'other-colors-items' found.")

    def extract_magento_data(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract the Magento script
        magento_script = soup.find_all('script', type='text/x-magento-init')
      
        if magento_script:
            for i in magento_script:
                try:
                    magento_data = json.loads(i.string)
                    self.magento_data = magento_data
                    # print(magento_data,end="\n"*3)
                    try:
                        #['data']['items']['406973']['ddg_categories']
                        ddg_categories = magento_data['*']['Magento_Catalog/js/product/view/provider']['data']['items']

                        # Print the categories
                        print("DDG Categories:")
                        for category in ddg_categories:
                            k=magento_data['*']['Magento_Catalog/js/product/view/provider']['data']['items'][category]
                            # for h in k:
                            print(k['extension_attributes'])
                    except:
                        pass
                        
                except json.JSONDecodeError as e:
                    print("Error decoding Magento JSON: " + str(e))
        else:
            print("Warning: No Magento script found.")

    def extract_data(self):
        html_content = self.fetch_page()
        self.extract_product_data(html_content)
        self.decode_other_colors_from_html(html_content)
        self.extract_magento_data(html_content)

        result = []
        if self.product_data:  # Check if product_data has a value
            result.append(self.product_data)
        if self.other_colors_data:  # Check if other_colors_data has a value
            result.append(self.other_colors_data)
        if self.magento_data:  # Check if magento_data has a value
            result.append(self.magento_data)

        return result

# Usage
url = "https://shop.bench.com.ph/bta0011bu2-mens-sports-tank-top"
extractor = ProductExtractor(url)
prd = extractor.extract_data()





