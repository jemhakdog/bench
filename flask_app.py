from flask import *
from werkzeug.utils import secure_filename  

import sqlite3

import os
app = Flask(__name__, static_url_path="", static_folder="static", template_folder="templates")

DATABASE = 'ecommerce.db'
from datetime import datetime
from typing import List, Dict, Any


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

# Database connection
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
UPLOAD_FOLDER = 'static/images'  # Change this to your desired folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
    
@app.route("/")
def index():
    products = get_all_products()
    results = []

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart')
    items = cursor.fetchall()
    conn.close()
    cart = [dict(item) for item in items]
    return render_template("index.html",cart=cart,cart_len=len(cart),products=products, get_product_by_id=get_product_by_id, get_existing_image_path=get_existing_image_path)


@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")

def getproduct(id: int) -> List[Dict[str, Any]]:
    """
    Retrieve detailed product information for a given product ID from the database.

    This function fetches all products and cart items from the database, processes
    the data to extract relevant information including images, data, and cart details,
    and returns a list of product information dictionaries for the product matching
    the specified ID.

    Args:
        id (int): The ID of the product to retrieve information for.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing detailed product information,
              including name, url, sku, brand, image, description, size, price, and other colors.
    """
    products = get_all_products()
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
                product_info: Dict[str, Any] = {}

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

    products=get_all_products()
    for product in products:
        product['images'] = json.loads(product['images'])
    return jsonify(results)


@app.route("/filter", methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        data = request.get_json()
        
        # Get database connection
        conn = get_db('ecommerce.db')
        cursor = conn.cursor()
        
        # Base query
        query = '''
            SELECT product_id, name, price, images, section, category, data 
            FROM products
        '''
        params = []
        
        # Add filters if present
        if data and 'categories' in data:
            selected_filters = data.get('categories', [])
            if selected_filters:
                filter_conditions = []
                for filter_id in selected_filters:
                    clean_filter = filter_id
                    for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
                        clean_filter = clean_filter.replace(prefix, '')
                    clean_filter = clean_filter.replace('-', ' ')
                    filter_conditions.append('(LOWER(section) LIKE ? OR LOWER(category) LIKE ?)')
                    params.extend([f'%{clean_filter.lower()}%', f'%{clean_filter.lower()}%'])
                
                if filter_conditions:
                    query += ' WHERE ' + ' OR '.join(filter_conditions)
        
        # Execute query
        cursor.execute(query, params)
        products = cursor.fetchall()
        data=""
        if not products:
            return "<h5>no products found!</h5>"
        for i in products:
            thedata = json.loads(i['data'])
            data+=f"""<div class="col-lg-4 product-item" id="{ i['product_id'] } { i['section']}-{ i['category']}">
                <div class="card border-0 shadow-sm rounded-3 mb-3">
                <!-- <img class="card-img-top w-100 d-block card-img-top rounded-top-3" src="{json.loads(i['images'])[0]}" alt="Product Image"> -->
                <!-- Main product image -->
                <img class="card-img-top w-100 d-block card-img-top rounded-top-3" src="{json.loads(i['images'])[0]}"
                    alt="Product Image" id="main-image"
                    onclick="window.location.href = `/product/view/{ i['product_id'] }`">

                <!-- Hover image for the same product -->
                <img class="card-img-top w-100 d-block card-img-top rounded-top-3 card-img-hover"
                    src="{ json.loads(i['images'])[1] }" alt="Product Image Hover" id="hover-image"
                    onclick="window.location.href = `/product/view/{ i['product_id'] }`">

                <div class="card-body">
                    <h5 class="fw-bold card-title mb-2">{ i['name'] }</h5>
                    <div class="d-flex justify-content-between align-items-center mb-3"><span class="fs-4 fw-bold">php { i['price'] }</span>
                    <!-- <div class="input-group input-group-sm" style="width:120px;"><button class="btn btn-outline-secondary"
                        type="button" id="decrease-quantity">-</button><input
                        class="form-control form-control text-center" type="number" id="quantity-input" min="1"
                        value="1"><button class="btn btn-outline-secondary" type="button"
                        id="increase-quantity">+</button>
                    </div> -->
                    <div class="input-group input-group-sm" style="width: 120px">
                        <button
                        class="btn btn-outline-secondary"
                        type="button"
                        onclick="updateQuantity(-1)"
                        >
                        -
                        </button>
                        <input
                        class="form-control form-control text-center"
                        type="number"
                        id="productQuantity"
                        name="productQuantity"
                        min="1"
                        value="1"
                        />
                        <button
                        class="btn btn-outline-secondary"
                        type="button"
                        onclick="updateQuantity(1)"
                        >
                        +
                        </button>
                    </div>
                    </div><button class="btn btn-primary w-100 rounded-pill" id="add-to-cart-btn" class="position-relative"
                    data-bs-toggle="modal" data-bs-target="#itemviewmodal">Add to Cart</button>
                </div>
                <div>
                    <input type="hidden" name="category" value="{ i['category'] }">
                    <input type="hidden" name="section" value="{ i['section'] }">
                </div>
                </div>
            </div>\n"""
        return data
    
@app.route("/shop")
@app.route("/shop/<int:page>", methods=['GET', 'POST'])
def shop(page=1):
    per_page = 20
    
    # Get database connection
    conn = get_db('ecommerce.db')
    cursor = conn.cursor()
    
    # Get total count for pagination
    cursor.execute('SELECT COUNT(*) FROM products')
    total = cursor.fetchone()[0]
    total_pages = (total + per_page - 1) // per_page
    page = min(max(1, page), total_pages)
    offset = (page - 1) * per_page
    
    # Base query
    query = '''
        SELECT product_id, name, price, images, section, category, data 
        FROM products
    '''
    params = []
    
    # Handle filters if present
    if request.method == 'POST' and request.is_json:
        filters = request.get_json().get('categories', [])
        if filters:
            filter_conditions = []
            for filter_id in filters:
                clean_filter = filter_id
                for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
                    clean_filter = clean_filter.replace(prefix, '')
                clean_filter = clean_filter.replace('-', ' ')
                filter_conditions.append('(LOWER(section) LIKE ? OR LOWER(category) LIKE ?)')
                params.extend([f'%{clean_filter.lower()}%', f'%{clean_filter.lower()}%'])
            
            if filter_conditions:
                query += ' WHERE ' + ' OR '.join(filter_conditions)
    
    # Add pagination
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    
    # Execute final query
    cursor.execute(query, params)
    products = cursor.fetchall()
    
    # Get cart items
    cart_conn = get_db_connection()
    cart_cursor = cart_conn.cursor()
    cart_cursor.execute('SELECT * FROM cart')
    cart_items = cart_cursor.fetchall()
    cart_conn.close()
    cart = [dict(item) for item in cart_items]
    
    # Process products
    processed_products = []
    for product in products:
        product_dict = dict(product)
        product_dict['images'] = json.loads(product_dict['images'])
        product_dict['data'] = json.loads(product_dict['data'])
        processed_products.append(product_dict)
    
    conn.close()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({
            'products': processed_products,
            'cart': cart,
            'cart_len': len(cart),
            'current_page': page,
            'total_pages': total_pages
        })
    
    return render_template(
        "menu.html",
        products=processed_products,
        cart=cart,
        cart_len=len(cart),
        current_page=page,
        total_pages=total_pages
    )


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
    products=get_all_products()
    for product in products:
        product['images'] = json.loads(product['images'])
    return render_template("admin-product.html",products=products)


 
@app.route("/product/view/<int:id>")
def view_product(id):

    products = get_all_products()
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
    conn = get_db('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    
    # Convert Row objects to a list of dictionaries
    products = [dict(row) for row in rows]
    
    conn.close()
    return jsonify(products)  


@app.route('/products/links')
def product_link():
    conn = get_db('ecommerce.db')
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
        conn = get_db('ecommerce.db')
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
    conn = get_db('ecommerce.db')
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
        
    conn = get_db('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (id,))
    conn.commit()
    conn.close()
   
    return redirect(url_for('index'))
#c===============cart===============



# Create a new cart item
@app.route('/cart/add', methods=['POST'])
def add_cart_item():
    """
    Add a new item to the cart.

    Parameters
    ----------
    data : dict
        A JSON object containing the following keys:
        - user_id: The ID of the user
        - product_id: The ID of the product
        - color: The color of the product
        - size: The size of the product
        - quantity: The quantity of the product to add
        - sku: The Stock Keeping Unit (SKU) of the product
        - image: The URL of the product's image
        - name: The name of the product
        - price: The price of the product

    Returns
    -------
    A JSON object with a "message" key containing a success message.
    """
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
    """
    Retrieve all cart items.

    Returns
    -------
    A JSON object containing a list of all cart items. Each item is represented as a dictionary with the following keys:
    - id: The item's ID
    - user_id: The user ID associated with this cart item
    - product_id: The product ID associated with this cart item
    - order_date: The date and time when the item was added to the cart
    - color: The color of the item
    - size: The size of the item
    - quantity: The quantity of the item in the cart
    - sku: The Stock Keeping Unit (SKU) of the item
    - image: The URL of the item's image
    - name: The name of the item
    - price: The price of the item
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart')
    items = cursor.fetchall()
    conn.close()
    return jsonify([dict(item) for item in items])

# Read a specific cart item
@app.route('/cart/<int:item_id>', methods=['GET'])
def get_cart_item(item_id):
    """
    Retrieve a specific cart item by its ID.

    Parameters
    ----------
    item_id : int
        The ID of the cart item to retrieve.

    Returns
    -------
    A JSON object representing the cart item if found, or a JSON object 
    with a 'message' key containing 'Item not found!' if the item does not exist.
    """
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
    """
    Update a cart item.
    
    Parameters
    ----------
    item_id : int
        The id of the item to update.
    
    Returns
    -------
    A JSON object with a "message" key containing a success message.
    """
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
    """
    Delete a cart item with the given item_id.

    Returns:
        A JSON object with a 'message' key containing 'Item deleted!'.
    """
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cart WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Item deleted!'}), 200



@app.errorhandler(401)
def unauthorized(e):
    return render_template('401.html'), 401

if __name__== "__main__":
	app.run(debug=True)