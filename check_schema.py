import sqlite3

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Get table info
cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='products';")
print(cursor.fetchone()[0])

conn.close()
