import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
connection = sqlite3.connect('cart.db')

# Create a cursor object using the cursor() method  
cursor = connection.cursor()

# Create tables
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS admins (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     email TEXT NOT NULL,
#     password TEXT NOT NULL,
#     full_name TEXT NOT NULL,
#     address TEXT NOT NULL,
#     phone_number TEXT NOT NULL
# )
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     email TEXT NOT NULL,
#     password TEXT NOT NULL,
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,    
#     address TEXT NOT NULL,
#     mode_of_payment TEXT NOT NULL,
#     phone_number TEXT NOT NULL
# )
# ''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     image TEXT NOT NULL,
#     name TEXT NOT NULL,
#     category TEXT NOT NULL,
#     price REAL NOT NULL,
#     rating INTEGER NOT NULL,
#     description TEXT NOT NULL,
#     stock INTEGER NOT NULL DEFAULT 0
# )
# ''')


# cursor.execute('''
# CREATE TABLE products (
#     product_id VARCHAR(50),
#     name VARCHAR(255) NOT NULL,
#     link VARCHAR(255) NOT NULL,
#     price DECIMAL(10, 2) NOT NULL,
#     images JSON NOT NULL,
#     section VARCHAR(100),   
#     category VARCHAR(100),
#     data JSON NOT NULL    
# );
# ''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS checkouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    checkout_date DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
''')

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS orders (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER NOT NULL,
#     product_id INTEGER NOT NULL,
#     order_date DATETIME NOT NULL,
#     status TEXT NOT NULL,
#     FOREIGN KEY (user_id) REFERENCES users(id),
#     FOREIGN KEY (product_id) REFERENCES products(id)
# )
# ''')


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
    image TEXT NOT NULL,
    name TEXT NOT NULL ,
    price INTEGER NOT NULL                
)
''')



# cursor.execute('''
# CREATE TABLE IF NOT EXISTS payments (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER NOT NULL,
#     order_id INTEGER NOT NULL,
#     payment_date DATETIME NOT NULL,
#     payment_method TEXT NOT NULL,
#     FOREIGN KEY (user_id) REFERENCES users(id),
#     FOREIGN KEY (order_id) REFERENCES orders(id)
# )
# ''')

# Commit the changes and close the connection
connection.commit()
connection.close()

