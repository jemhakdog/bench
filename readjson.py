import json
import sqlite3
from indiviualitemscrapper import ProductExtractor
# Connect to SQLite database (it will create the database file if it doesn't exist)
connection = sqlite3.connect('ecommerce.db')

# Create a cursor object using the cursor() method  
cursor = connection.cursor()

class CategoryExtractor:
    def __init__(self, file_path):
        """
        Initializes the CategoryExtractor with the path to the JSON file.
        
        :param file_path: Path to the JSON file to be read.
        """
        self.file_path = file_path
        self.data = self.load_data()
        self.cat1 = []
        self.cat2 = []

    def load_data(self):
        """
        Loads data from the JSON file.
        
        :return: Parsed JSON data as a dictionary.
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def extract_categories(self):
        """
        Extracts categories from the loaded data and populates cat1 and cat2.
        """
        for key in self.data:
            self.cat1.append(key)
            li = []
            for item in self.data[key]:
                li.append(item)
            self.cat2.append({key: li})
        print("cat2;",self.cat2)

    def get_categories(self):
        """
        Returns the extracted categories.
        
        :return: A tuple containing cat1 and cat2.
        """
        return self.cat1, self.cat2
    def get(self,category,key):
        print(self.data[category][key][key][0])

    def create_database(self):
        """
        Extracts categories from the loaded data and populates cat1 and cat2.
        """
        self.products_data=[]
       
        for key in self.data:
            for item in self.data[key]:
                for i in self.data[key][item][item]:
                        product_id = str(i['product_id'])
                        name = i['name'].replace("'", "''")
                        link = i['link'].replace("'", "''")
                        price = i['price']  # Assuming price is a float or int, no quotes needed
                        images_json = json.dumps(i['images']).replace("'", "''")
                        section = key.replace("'", "''")
                        category = item.replace("'", "''")

                        extractor = ProductExtractor(i['link'])
                        data_extracted = json.dumps(extractor.extract_data()).replace("'", "''")

                        # Create a dictionary for the product data
                        product_data = {
                            'product_id': product_id,
                            'name': name,
                            'link': link,
                            'price': price,
                            'images': images_json,
                            'section': section,
                            'category': category,
                            'data': data_extracted
                        }

                        # Append the product data to the list
                        self.products_data.append(product_data)

                    # Write the products data to a JSON file
                    
                    # product_id = str(i['product_id'])
                    # name = i['name'].replace("'", "''")
                    # link = i['link'].replace("'", "''")
                    # price = i['price']  # Assuming price is a float or int, no quotes needed
                    # images_json = json.dumps(i['images']).replace("'", "''")
                    # section = key.replace("'", "''")
                    # category = item.replace("'", "''")

                    # extractor = ProductExtractor(i['link'])
                    # data_extracted = json.dumps(extractor.extract_data()).replace("'", "''")

                    # try:
                    #     # Prepare the SQL statement
                    #     sql = f'''
                    #     INSERT OR IGNORE INTO products (product_id, name, link, price, images, section, category,data)
                    #     VALUES (
                    #         '{product_id}',
                    #         '{name}',
                    #         '{link}',
                    #         {price},
                    #         '{images_json}',
                    #         '{section}',
                    #         '{category}',
                    #         '{data_extracted}'
                    #     );
                    #     '''
                    #     cursor.execute(sql)
                        
                    # except:
                    #     pass

    


           

# Example usage
if __name__ == "__main__":
    try:
        extractor = CategoryExtractor('bench-products.json')
        extractor.extract_categories()
        categories = extractor.get_categories()
       
        extractor.create_database()
        with open('products.json', 'w') as json_file:
            json.dump(extractor.products_data, json_file, indent=4)
        # connection.commit()
        # connection.close()
    except:

        # connection.commit()
        # connection.close()
        pass

    # extractor.get("women","underwear-loungewear")