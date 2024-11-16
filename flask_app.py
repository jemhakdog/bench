from flask import *
from werkzeug.utils import secure_filename  

import sqlite3

import os
app = Flask(__name__, static_url_path="", static_folder="static", template_folder="templates")

DATABASE = 'ecommerce.db'
import os
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Database connection
def get_db_connection():
    conn = sqlite3.connect('cart.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the cart table
def create_table():
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

create_table()
from datetime import datetime


UPLOAD_FOLDER = 'static/images'  # Change this to your desired folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def get_existing_image_path(product_id):
    conn = get_db()  # Get a connection to the database
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

def get_product_list():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    
    # Convert Row objects to a list of dictionaries
    products = [dict(row) for row in rows]
    
    conn.close()
    return products

def get_product_by_id(product_id):
    conn = get_db()
    cursor = conn.cursor()
    
    # Use a parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()
    
    conn.close()
    
    # Check if a row was found and convert it to a dictionary if it exists
    if row:
        return dict(row)
    else:
        return None  # or raise an exception or return an appropriate message
    
@app.route("/")
def index():
    products = get_product_list()
    results = []

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart')
    items = cursor.fetchall()
    conn.close()
    cart = [dict(item) for item in items]
    return render_template("index.html",cart=cart,cart_len=len(cart),products=products,os=os)


@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")


def getproduct(id):
     
    products = get_product_list()
    results = []

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart')
    items = cursor.fetchall()
    conn.close()
    cart = [dict(item) for item in items]


    for product in products:
        product['images'] = json.loads(product['images']) 
        product['data'] = json.loads(product['data']) # get all products

      
    
    for product in products:#only return the product with the matching id
        print(product['product_id'])
        if int(product['product_id']) == int(id):
            for item in product['data']:
                # Create a dictionary to hold the extracted information
                product_info = {}

                # Extract the specified keys
                for key in ["name", "url", "sku", "brand", "image", "description", "size"]:
                    if key in item:
                        product_info[key] = item[key]

                # Extract and store the price from 'offers' if it exists
                if 'offers' in item and 'price' in item['offers']:
                    product_info['price'] = item['offers']['price']

                # Extract 'other-colors' if it exists
                if 'other-colors' in item:
                    product_info['other-colors'] = []
                    for color in item['other-colors']['products']:
                        # Assuming each color has 'url', 'image_url', and 'variant'
                        color_info = {
                            'url': color.get('url'),
                            'image_url': color.get('image_url'),
                            'variant': color.get('variant')
                        }
                        product_info['other-colors'].append(color_info)

                # Append the product information to results
                results.append(product_info)

    products=get_product_list()
    for product in products:
        product['images'] = json.loads(product['images'])
    return results
@app.route("/shop")
def shop():
    
    products = get_product_list()
    results = []

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart')
    items = cursor.fetchall()
    conn.close()
    cart = [dict(item) for item in items]


    for product in products:
        product['images'] = json.loads(product['images']) 
        product['data'] = json.loads(product['data']) # get all products

      
    


    products=get_product_list()
    for product in products:
        product['images'] = json.loads(product['images'])
    return render_template("menu.html",products=products,cart=cart,cart_len=len(cart),os=os,results=results)


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/account-recovery")
def account_recovery():
    return render_template("account-recovery.html")


@app.route("/admin")
def admin():
    products=get_product_list()
    for product in products:
        product['images'] = json.loads(product['images'])
    return render_template("admin-product.html",products=products)


 
@app.route("/product/view/<int:id>")
def view_product(id):

    products = get_product_list()
    results = []

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart')
    items = cursor.fetchall()
    conn.close()
    cart = [dict(item) for item in items]


    for product in products:
        product['images'] = json.loads(product['images']) 
        product['data'] = json.loads(product['data']) # get all products

      
    
    for product in products:#only return the product with the matching id
        print(product['product_id'])
        if int(product['product_id']) == int(id):
            for item in product['data']:
                # Create a dictionary to hold the extracted information
                product_info = {}

                # Extract the specified keys
                for key in ["name", "url", "sku", "brand", "image", "description", "size"]:
                    if key in item:
                        product_info[key] = item[key]

                # Extract and store the price from 'offers' if it exists
                if 'offers' in item and 'price' in item['offers']:
                    product_info['price'] = item['offers']['price']

                # Extract 'other-colors' if it exists
                if 'other-colors' in item:
                    product_info['other-colors'] = []
                    for color in item['other-colors']['products']:
                        # Assuming each color has 'url', 'image_url', and 'variant'
                        color_info = {
                            'url': color.get('url'),
                            'image_url': color.get('image_url'),
                            'variant': color.get('variant')
                        }
                        product_info['other-colors'].append(color_info)

                # Append the product information to results
                results.append(product_info)
            if len(results)>1:
                return render_template("pv.html", product=product,data=results[0],colors=results[1]["other-colors"],id=id,cart=cart,cart_len=len(cart),os=os)
            else:
                return render_template("pv.html", product=product,data=results[0],colors=[],id=id,cart=cart,cart_len=len(cart),os=os)
            
    # If product is not found, return a 404 error
    return "not founbd" 


@app.route('/products')
def products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    
    # Convert Row objects to a list of dictionaries
    products = [dict(row) for row in rows]
    
    conn.close()
    return jsonify(products)  


@app.route('/products/links')
def product_link():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    
    # Convert Row objects to a list of dictionaries
    products = [dict(row) for row in rows]
    
    conn.close()
    return jsonify(products) 


@app.route('/products/add', methods=['GET', 'POST'])
def add_product():

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        section = request.form.get('section', '')  # Optional field
        images = []  # Initialize images list

        # Process uploaded images
        if 'images' in request.files:
            image_files = request.files.getlist('images')  # Get list of uploaded images
            for image in image_files:
                if image:
                    image_filename = secure_filename(image.filename)  # Secure the filename
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
                    image.save(image_path)  # Save the image file
                    images.append(image_filename)  # Append filename to images list

        # Convert images list to JSON
        images_json = json.dumps(images)

        # Database insertion
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO products (product_id, name, link, price, images, section, category) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (None, name, '', price, images_json, section, category))  # Assuming product_id is auto-generated
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return True

@app.route('/products/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    conn = get_db()
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        rating = request.form['rating']
        description = request.form['description']
        stock = request.form['stock']
        image=request.files['image']
        category=request.form['category']
        if image:
        # Define the upload folder and filename
            upload_folder = 'static/images' # Set your upload folder
            filename = secure_filename(image.filename)  # Ensure the filename is safe
            image_path = os.path.join(upload_folder, filename)
        # Save the file
            image.save(image_path)
            image=image_path
        else:
            # If no new image, you might want to retrieve the existing image path from the database
            # For example:
            print('exisstttiinngg')
            existing_image_path = get_existing_image_path(id)  # Implement this function to get the current image path
            image   = existing_image_path
        cursor.execute("UPDATE products SET name=?,category=?,image=?, price=?, rating=?, description=?, stock=? WHERE id=?",
                       (name, category, image, price, rating, description, stock, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM products WHERE id=?", (id,))
        product = cursor.fetchone()
        conn.close()
        return render_template('edit_product.html', product=product)

@app.route('/products/delete/<int:id>', methods=['POST'])
def delete_product(id):
    product = get_product_by_id(id)
    
    if product:
        # Construct the full path to the image file
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], product['image'])
        
        # Remove the image file from the filesystem
        if os.path.exists(image_path):
            os.remove(image_path)
        
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()
    conn.close()
   
    return redirect(url_for('index'))
#c===============cart===============



# Create a new cart item
@app.route('/cart/add', methods=['POST'])
def add_cart_item():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cart (user_id, product_id, order_date, color, size, quantity, sku, image,name,price) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?,?, ?)
    ''', (data['user_id'], data['product_id'], datetime.now(), data['color'], data['size'], data['quantity'], data['sku'], data['image'],data['name'],data['price']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Item added to cart!'}), 201

# Read all cart items
@app.route('/cart', methods=['GET'])
def get_cart_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart')
    items = cursor.fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])

# Read a specific cart item
@app.route('/cart/<int:item_id>', methods=['GET'])
def get_cart_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart WHERE id = ?', (item_id,))
    item = cursor.fetchone()
    conn.close()
    if item:
        return jsonify(dict(item))
    else:
        return jsonify({'message': 'Item not found!'}), 404

# Update a cart item
@app.route('/cart/<int:item_id>', methods=['PUT'])
def update_cart_item(item_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE cart SET user_id = ?, product_id = ?, color = ?, size = ?, quantity = ?, sku = ?, image = ?
        WHERE id = ?
    ''', (data['user_id'], data['product_id'], data['color'], data['size'], data['quantity'], data['sku'], data['image'], item_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Item updated!'}), 200

# Delete a cart item
@app.route('/cart/<int:item_id>', methods=['DELETE'])
def delete_cart_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cart WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Item deleted!'}), 200



if __name__== "__main__":
	app.run(debug=True)

