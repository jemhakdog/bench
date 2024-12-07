# import json

# # Open and read the JSON file
# with open("products.json", 'r') as file:
#     products = json.load(file)

# # Initialize a list to hold the results
# results = []

# # Iterate through each product in the JSON data
# for product in products:
#     # Assuming 'data' is a key in each product dictionary
#     if "data" in product:
#         # Load the data if it's a JSON string
#         data = json.loads(product["data"])
#         for item in data:
#             # Create a dictionary to hold the extracted information
#             product_info = {}

#             # Extract the specified keys
#             for key in ["name", "url", "sku", "brand", "image", "description", "size"]:
#                 if key in item:
#                     product_info[key] = item[key]

#             # Extract and store the price from 'offers' if it exists
#             if 'offers' in item and 'price' in item['offers']:
#                 product_info['price'] = item['offers']['price']

#             # Extract 'other-colors' if it exists
#             if 'other-colors' in item:
#                 product_info['other-colors'] = []
#                 for color in item['other-colors']['products']:
#                     # Assuming each color has 'url', 'image_url', and 'variant'
#                     color_info = {
#                         'url': color.get('url'),
#                         'image_url': color.get('image_url'),
#                         'variant': color.get('variant')
#                     }
#                     product_info['other-colors'].append(color_info)

#             # Append the product information to results
#             results.append(product_info)

#     break 

# # Print the results dictionary
# print(json.dumps(results, indent=4))


# # import sqlite3
# # import json

# # # Connect to SQLite database (or create it)
# # conn = sqlite3.connect('bench.db')
# # cursor = conn.cursor()

# # # Open and read the JSON file
# # with open("products.json", 'r') as file:
# #     products = json.load(file)

# # # Loop through each product in the JSON data
# # for json_data in products:
# #     # Extract data from JSON
# #     product_id = json_data["product_id"]
# #     name = json_data["name"]
# #     link = json_data["link"]
# #     price = float(json_data["price"].replace('₱', '').replace(',', '').strip())  # Convert price to float
# #     images = json.dumps(json_data["images"])  # Convert images list to JSON string
# #     section = json_data["section"]
# #     category = json_data["category"]
# #     data = json.dumps(json_data["data"])  # Convert data list to JSON string

# #     # Insert data into the database
# #     cursor.execute('''
# #     INSERT INTO products (product_id, name, link, price, images, section, category, data)
# #     VALUES (?, ?, ?, ?, ?, ?, ?, ?)
# #     ''', (product_id, name, link, price, images, section, category, data))

# # # Commit the changes and close the connection
# # conn.commit()
# # conn.close()

# # print("Data inserted successfully.")


# import json
# import requests
# import os

# # Open and read the JSON file
# with open("products.json", 'r') as file:
#     products = json.load(file)

# # Create a directory to save images
# os.makedirs("bench", exist_ok=True)

# # Loop through the products and download images
# for product in products:
#     images = product["images"]
#     for index, image_url in enumerate(images):
#         # Get the image content
#         response = requests.get(image_url)
#         if response.status_code == 200:
#             # Create a filename based on the product and index
#             filename = os.path.join("bench", image_url)
#             # Write the image to a file
#             with open(filename, 'wb') as img_file:
#                 img_file.write(response.content)
#             print(f"Downloaded: {filename}")
#         else:
#             print(f"Failed to download: {image_url}")



import json
import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to download a single image
def download_image(image_url):
   
    # if not (image_url.startswith('http://') or image_url.startswith('https://')):
    #     return f"Invalid URL: {image_url}. Skipping download."

    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            # Create a filename based on the image URL
            filename = os.path.join("bench", os.path.basename(image_url))
            # Write the image to a file
            with open(filename, 'wb') as img_file:
                img_file.write(response.content)
            return f"Downloaded: {filename}"
        else:
            return f"Failed to download: {image_url} (Status code: {response.status_code})"
    except Exception as e:
        return f"Error downloading {image_url}: {e}"

# Open and read the JSON file
with open("products.json", 'r') as file:
    products = json.load(file)

# Create a directory to save images
os.makedirs("bench", exist_ok=True)

# List to hold all image URLs
image_urls = []

# Collect all image URLs from products
for product in products:
    images = json.loads(product.get("images"))
    image_urls.extend(images)

# Use ThreadPoolExecutor to download images concurrently
with ThreadPoolExecutor(max_workers=100) as executor:
    # Submit all download tasks
    future_to_url = {executor.submit(download_image, url): url for url in image_urls}
    
    # Process results as they complete
    for future in as_completed(future_to_url):
        result = future.result()


def odd