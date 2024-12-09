import math
from flask import Flask, render_template, request, redirect, jsonify, url_for
from werkzeug.utils import secure_filename  
from datetime import datetime
from typing import List, Dict, Any
import sqlite3
import os
import json

app = Flask(__name__, static_url_path="", static_folder="static", template_folder="templates")
app.config['UPLOAD_FOLDER'] = 'static/images'
DATABASE = 'ecommerce.db'
cartDB = 'cart.db'
per_page = 20

def get_db(database):
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db(cartDB)
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
        image TEXT NOT NULL,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def db_query(query, params=[], fetchone=False, commit=False, db=DATABASE):
    conn = get_db(db)
    cursor = conn.cursor()
    cursor.execute(query, params)
 
    conn.commit()
    result = cursor.fetchone() if fetchone else cursor.fetchall()
    conn.close()
    return result

def get_all_products():
    products = db_query("SELECT * FROM products")
    return [dict(row) for row in products]

def get_product_details(product_id):
    product = db_query("SELECT * FROM products WHERE product_id = ?", [product_id], fetchone=True)
    if product:
        return dict(product)
    return None

create_table()

@app.route("/")
def index():
    products = get_all_products()
    cart = db_query('SELECT * FROM cart', db=cartDB)
    return render_template("index.html", cart=[dict(item) for item in cart], cart_len=len(cart), products=products, get_product_by_id=get_product_details)
@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/account-recovery")
def account_recovery():
    return render_template("account-recovery.html")
@app.route("/product/view/<int:id>")
def view_product(id):
    product = get_product_details(id)
    if not product:
        return "Product not found", 404
    return render_template("pv.html", product=product)

@app.route("/product/add", methods=['POST'])
def add_product():
    name = request.form['name']
    price = request.form['price']
    category = request.form['category']
    section = request.form.get('section', '')
    image = request.files['image']
    image_filename = None if not image else secure_filename(image.filename)
    if image_filename:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        image.save(image_path)
    db_query("INSERT INTO products (name, price, category, section, images) VALUES (?, ?, ?, ?, ?)", (name, price, category, section, json.dumps([image_filename])), commit=True)
    return redirect(url_for('index'))

@app.route('/cart/<int:item_id>', methods=['POST', 'PUT', 'DELETE'])
def cart_item(item_id):
    if request.method == 'POST':
        data = request.get_json()
        db_query('INSERT INTO cart (user_id, product_id, order_date, color, size, quantity, sku, image, name, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                 [data['user_id'], data['product_id'], datetime.now(), data['color'], data['size'], data['quantity'], data['sku'], data['image'], data['name'], data['price']],
                 commit=True, db=cartDB)
        return jsonify({'message': 'Item added to cart!'}), 201
    elif request.method == 'PUT':
        data = request.get_json()
        db_query('UPDATE cart SET user_id = ?, product_id = ?, color = ?, size = ?, quantity = ?, sku = ?, image = ?, name = ?, price = ? WHERE id = ?', 
                 [data['user_id'], data['product_id'], data['color'], data['size'], data['quantity'], data['sku'], data['image'], data['name'], data['price'], item_id],
                 commit=True, db=cartDB)
        return jsonify({'message': 'Item updated!'}), 200
    elif request.method == 'DELETE':
        db_query('DELETE FROM cart WHERE id = ?', [item_id], commit=True, db=cartDB)
        return jsonify({'message': 'Item deleted!'}), 200

@app.route('/cart')
def get_cart_items():
    cart = db_query('SELECT * FROM cart', db=cartDB)
    return jsonify([dict(item) for item in cart])

@app.route("/pagination", methods=['GET', 'POST'])
def pagination():
    page = request.args.get('page', 1, type=int)
    data = request.get_json()
    min_price = request.form.get('min')
    max_price = request.form.get('max')

    query = '''
        SELECT product_id, name, price, images, section, category, data
        FROM products
    '''
    params = []

    if data and 'categories' in data:
        selected_filters = data.get('categories', [])
        if selected_filters:
            filter_conditions = []
            for filter_id in selected_filters:
                clean_filter = filter_id
                for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
                    if clean_filter.startswith(prefix):
                        the_category = clean_filter.replace(prefix, '')
                        the_section = prefix[:-1]
                        filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
                        params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])
            query += ' WHERE ' + ' OR '.join(filter_conditions)

    if min_price and max_price:
        query += ' AND ' if 'WHERE' in query else ' WHERE '
        query += 'price BETWEEN ? AND ?'
        params.extend([min_price, max_price])

    products = db_query(query, params)
    total_products = len(products)
    total_pages = math.ceil(total_products / per_page)

    processed_products = []
    for product in products:
        product_dict = dict(product)
        try:
            product_dict['images'] = json.loads(product_dict['images'])
        except json.JSONDecodeError:
            product_dict['images'] = []
        processed_products.append(product_dict)

    return jsonify({
        'products': processed_products,
        'pagination': {
            'current_page': page,
            'total_pages': total_pages,
            'total_products': total_products
        }
    }), 200

@app.route("/api/shop_data", methods=['GET', 'POST'])
def api_shop_data():
    try:
        page = int(request.args.get('page', 1))
        per_page = 20
        offset = (page - 1) * per_page

        conn = get_db('ecommerce.db')
        cursor = conn.cursor()

        query = '''
            SELECT product_id, name, price, images, section, category, data
            FROM products
        '''
        params = []

        categories_param = request.args.get('categories')
        if categories_param:
            try:
                selected_categories = json.loads(categories_param)
                if selected_categories:
                    category_conditions = []
                    for category in selected_categories:
                        clean_category = category.split('-')[-1]
                        category_conditions.append(
                            '(LOWER(section) LIKE ? OR LOWER(category) LIKE ?)'
                        )
                        params.extend([f'%{clean_category.lower()}%', f'%{clean_category.lower()}%'])

                    query += ' WHERE ' + ' OR '.join(category_conditions)
            except json.JSONDecodeError:
                pass

        min_price = request.args.get('minPrice')
        max_price = request.args.get('maxPrice')
        if min_price and max_price:
            if 'WHERE' in query:
                query += ' AND price BETWEEN ? AND ?'
            else:
                query += ' WHERE price BETWEEN ? AND ?'
            params.extend([min_price, max_price])

        count_query = f"SELECT COUNT(*) as total FROM ({query}) as filtered_products"
        cursor.execute(count_query, params)
        total_products = cursor.fetchone()['total']

        query += ' LIMIT ? OFFSET ?'
        params.extend([per_page, offset])

        cursor.execute(query, params)
        products = cursor.fetchall()

        processed_products = []
        for product in products:
            product_dict = dict(product)
            try:
                product_dict['images'] = json.loads(product_dict['images'])
            except json.JSONDecodeError:
                product_dict['images'] = []

            processed_products.append(product_dict)

        total_pages = (total_products + per_page - 1) // per_page

        return jsonify({
            'products': processed_products,
            'pagination': {
                'current_page': page,
                'total_pages': total_pages,
                'total_products': total_products
            }
        }), 200

    except Exception as e:
        return jsonify({'error': 'Failed to fetch shop data'}), 500

@app.route("/filter", methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        data = request.get_json()

        min_price = request.form.get('min')
        max_price = request.form.get('max')

        conn = get_db('ecommerce.db')
        cursor = conn.cursor()

        query = '''
            SELECT product_id, name, price, images, section, category, data
            FROM products
        '''
        params = []

        if data and 'categories' in data:
            selected_filters = data.get('categories', [])
            if selected_filters:
                filter_conditions = []
                for filter_id in selected_filters:
                    clean_filter = filter_id
                    for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
                        if clean_filter.startswith(prefix):
                            the_category = clean_filter.replace(prefix, '')
                            the_section = prefix[:-1]
                            filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
                            params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])
                if filter_conditions:
                    query += ' WHERE ' + ' OR '.join(filter_conditions)

        if min_price and max_price:
            if 'WHERE' in query:
                query += ' AND price BETWEEN ? AND ?'
            else:
                query += ' WHERE price BETWEEN ? AND ?'
            params.extend([min_price, max_price])

        cursor.execute(query, params)
        products = cursor.fetchall()

        processed_products = []
        for product in products:
            product_dict = dict(product)
            try:
                product_dict['images'] = json.loads(product_dict['images'])
            except json.JSONDecodeError:
                product_dict['images'] = []

            processed_products.append(product_dict)

        page = request.args.get('page', 1, type=int)
        offset = (page - 1) * per_page
        query += ' LIMIT ? OFFSET ?'
        params.extend([per_page, offset])

        cursor.execute(query, params)
        products_paginated = cursor.fetchall()

        data = ""
        for i in products_paginated:
            product_data = json.loads(i['data'])
            data += f"""<div class="col-lg-4 product-item" id="{ i['product_id'] } { i['section']}-{ i['category']}">
                <div class="card border-0 shadow-sm rounded-3 mb-3">
                <img class="card-img-top w-100 d-block card-img-top rounded-top-3" src="{json.loads(i['images'])[0]}" alt="Product Image">
                <div class="card-body">
                    <h5 class="fw-bold card-title mb-2">{ i['name'] }</h5>
                    <div class="d-flex justify-content-between align-items-center mb-3"><span class="fs-4 fw-bold">php { i['price'] }</span>
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
    page = int(request.args.get('page', page))

    conn = get_db('ecommerce.db')
    cursor = conn.cursor()

    query = '''
        SELECT product_id, name, price, images, section, category, data
        FROM products
    '''
    params = []

    if request.method == 'POST' and request.is_json:
        filters = request.get('categories', [])
        if filters:
            filter_conditions = []
            for filter_id in filters:
                clean_filter = filter_id
                for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
                    if clean_filter.startswith(prefix):
                        the_category = clean_filter.replace(prefix, '')
                        the_section = prefix[:-1]
                        filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
                        params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])
            if filter_conditions:
                query += ' WHERE ' + ' OR '.join(filter_conditions)

    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])

    cursor.execute(query, params)
    products = cursor.fetchall()

    processed_products = []
    for product in products:
        product_dict = dict(product)
        product_dict['images'] = json.loads(product_dict['images'])
        product_dict['data'] = json.loads(product_dict['data'])
        processed_products.append(product_dict)

    cart_conn = get_db_connection()
    cart_cursor = cart_conn.cursor()
    cart_cursor.execute('SELECT * FROM cart')
    cart_items = cart_cursor.fetchall()
    cart_conn.close()
    cart = [dict(item) for item in cart_items]

    conn.close()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({
            'products': processed_products,
            'cart': cart,
            'cart_len': len(cart),
            'current_page': page,
            'total_pages': total_pages
        })

    pagination_links = generate_pagination_links(page, total_pagez.get_total_pages())
    if request.method == 'GET':
        pagination_links = generate_pagination_links(page, total_pagez.get_total_pages())

    return render_template(
        "menu.html",
        products=processed_products,
        cart=cart,
        cart_len=len(cart),
        current_page=page,
        total_pages=total_pagez.get_total_pages(),
        pagination_links=pagination_links,
    )

@app.route('/api/products')
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = 9

    products = Product.query.paginate(page=page, per_page=per_page)

    return jsonify({
        'products': [product.to_dict() for product in products.items],
        'pagination': {
            'current_page': page,
            'total_pages': products.pages,
            'total_items': products.total
        }
    })

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

# @app.route('/cart', methods=['GET'])
# def get_cart_items():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM cart')
#     items = cursor.fetchall()
#     conn.close()
#     return jsonify([dict(item) for item in items])

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

@app.route('/cart/<int:item_id>', methods=['DELETE'])
def delete_cart_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cart WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Item deleted!'}), 200

@app.route("/products/edit/<int:id>", methods=['GET', 'POST'])
def edit_product(id):
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        section = request.form.get('section', '')
        image = request.files['image']
        image_filename = None if not image else secure_filename(image.filename)
        if image_filename:
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            image.save(image_path)
        db_query("UPDATE products SET name=?, price=?, category=?, section=?, images=? WHERE product_id=?", 
                 [name, price, category, section, json.dumps([image_filename]), id], commit=True)
        return redirect(url_for('index'))
    else:
        product = get_product_by_id(id)
        return render_template('edit_product.html', product=product)

@app.route('/products/delete/<int:id>', methods=['POST'])
def delete_product(id):
    product = get_product_by_id(id)

    if product:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], product['image'])
        if os.path.exists(image_path):
            os.remove(image_path)

    db_query("DELETE FROM products WHERE product_id=?", [id], commit=True)
    return redirect(url_for('index'))

@app.route("/products/add", methods=['GET', 'POST'])
def add_product_route():
    return add_product()

if __name__ == "__main__":
    app.run(debug=True)
