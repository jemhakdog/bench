import sqlite3
from typing import List, Dict, Any
import json

def get_db(DATABASE):
    """
    Connect to the SQLite database (DATABASE) and return the connection object.

    The connection object is a sqlite3.Connection object, which is used to execute
    SQL queries, create tables, insert data, etc.

    :param DATABASE: The path to the SQLite database file.
    :return: A sqlite3.Connection object.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_db_connection():
    """
    Connect to the SQLite database (cart.db) and return the connection object.

    The connection object is a sqlite3.Connection object, which is used to execute
    SQL queries and perform other database operations.

    The row_factory of the connection is set to sqlite3.Row, which allows us to
    access the query results as dictionaries.

    Returns:
        sqlite3.Connection
    """
    conn = sqlite3.connect('cart.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_cart_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        order_date DATETIME NOT NULL,
        color TEXT NOT NULL,
        size TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        sku TEXT NOT NULL,
        image TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def get_existing_image_path(product_id):
    conn = get_db('ecommerce.db')  # Get a connection to the database
    cursor = conn.cursor()

    # Execute a query to get the image path for the specified product ID
    cursor.execute("SELECT image FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()

    conn.close()  # Close the database connection

    # Check if a row was found and return the image path if it exists
    if row:
        return row['image']  # Return the image filename or path
    else:
        return None  # Return None if no product was found

def get_all_products():
    """Retrieve a list of all products from the database."""
    connection = get_db('ecommerce.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    product_rows = cursor.fetchall()

    # Convert Row objects to a list of dictionaries
    products = [dict(row) for row in product_rows]

    connection.close()
    return products

def get_product_by_id(product_id: int) -> dict | None:
    product_id = int(product_id)
    """
    Retrieve a product from the database by its ID.

    :param product_id: The ID of the product to retrieve.
    :return: A dictionary containing the product details if found, else None.
    """
    conn = get_db('ecommerce.db')
    cursor = conn.cursor()

    # Use a parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM products WHERE product_id = ?", (product_id,))
    row = cursor.fetchone()

    conn.close()

    # Check if a row was found and convert it to a dictionary if it exists
    if row:
        return dict(row)
    else:
        return []  # or raise an exception or return an appropriate message