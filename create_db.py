
import sqlite3

def create_database_and_tables():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            role TEXT NOT NULL CHECK(role IN ('admin', 'user')),
            email TEXT UNIQUE NOT NULL,
            phone_number TEXT NOT NULL,
            age INTEGER NOT NULL,
            birthday DATE NOT NULL,
            full_name TEXT NOT NULL,
            mode_of_payment TEXT NOT NULL CHECK(mode_of_payment IN ('gcash', 'cod'))
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Carts (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES Users(id)
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Ordered_Items (
            id INTEGER PRIMARY KEY,
            cart_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (cart_id) REFERENCES Carts(id),
            FOREIGN KEY (product_id) REFERENCES Products(id)
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            id INTEGER PRIMARY KEY,
            cart_id INTEGER NOT NULL,
            order_date DATE NOT NULL,
            total_cost REAL NOT NULL,
            FOREIGN KEY (cart_id) REFERENCES Carts(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database_and_tables()
