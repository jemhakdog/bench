import sqlite3
import json

# Product data
product = {
    'name': "Men's Irregular-Shaped Eyeglasses",
    'link': '',
    'price': 1200,
    'images': json.dumps([]),  # No images provided in task
    'section': 'men',
    'category': 'eyeglasses',
    'data': json.dumps({})  # No additional data provided in task
}

# Connect to database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Insert the product
cursor.execute("""
    INSERT INTO products (name, link, price, images, section, category, data)
    VALUES (:name, :link, :price, :images, :section, :category, :data)
""", product)

# Commit and close
conn.commit()
conn.close()

print("Product added successfully!")
