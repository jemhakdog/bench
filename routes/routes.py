# This file will contain all the routes extracted from flask_app.py

from flask import request, jsonify, render_template, redirect, url_for
from . import app
from .flask_app import (
    get_all_products, 
    get_product_by_id, 
    get_existing_image_path, 
    generate_pagination_links, 
    current_page, 
    filterz, 
    total_pagez, 
    get_db, 
    get_db_connection
)

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
    return render_template("index.html", cart=cart, cart_len=len(cart), products=products, get_product_by_id=get_product_by_id, get_existing_image_path=get_existing_image_path)

@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")

@app.route("/pagination", methods=['GET', 'POST'])
def pagination():
    if request.method == 'POST':
        page = request.args.get('page', 1, type=int)
        current_page.set_current_page(page)

        data = request.get_json()
        try:
            min = request.form['min']
            max = request.form['max']
        except:
            min = None
            max = None

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

        if min and max:
            query += ' WHERE price BETWEEN ? AND ?'
            params.append(min)
            params.append(max)

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

        per_page = 20
        total_pages = math.ceil(len(products) / per_page)

        count_query = f"SELECT COUNT(*) as total FROM ({query}) as filtered_products"
        cursor.execute(count_query, params)
        total_products = cursor.fetchone()['total']

        return jsonify({
            'products': processed_products,
            'pagination': {
                'current_page': page,
                'total_pages': total_pages,
                'total_products': total_products
            }
        }), 200

@app.route("/filter", methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        data = request.get_json()

        filterz.set_current_filters(data.get('categories'))
        try:
            min = request.form['min']
            max = request.form['max']
        except:
            min = None
            max = None

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

        if min and max:
            if 'WHERE' in query:
                query += ' AND price BETWEEN ? AND ?'
            else:
                query += ' WHERE price BETWEEN ? AND ?'
            params.append(min)
            params.append(max)

        cursor.execute(query, params)
        total = len(cursor.fetchall())

        per_page = 20
        total_pages = (total + per_page - 1) // per_page
        total_pagez.set_total_pages(total_pages)

        page = request.args.get('page', 1, type=int)
        offset = (page - 1) * per_page

        query += ' LIMIT ? OFFSET ?'
        params.extend([per_page, offset])

        cursor.execute(query, params)
        products = cursor.fetchall()

        data = ""
        if not products:
            return "<h5>no products found!</h5>"

        for i in products:
            thedata = json.loads(i['data'])
            data += f"""<div class="col-lg-4 product-item" id="{i['product_id']} {i['section']}-{i['category']}">
                <div class="card border-0 shadow-sm rounded-3 mb-3">
                <img class="card-img-top w-100 d-block card-img-top rounded-top-3" src="{json.loads(i['images'])[0]}"
                    alt="Product Image" id="main-image"
                    style="height: 401px;"
                    onclick="window.location.href = `/product/view/{i['product_id']}`">

                <img class="card-img-top w-100 d-block card-img-top rounded-top-3 card-img-hover"
                    src="{json.loads(i['images'])[1]}" alt="Product Image Hover" id="hover-image"
                       style="height: 401px;"
                    onclick="window.location.href = `/product/view/{i['product_id']}`">

                <div class="card-body">
                    <h5 class="fw-bold card-title mb-2">{i['name']}</h5>
                    <div class="d-flex justify-content-between align-items-center mb-3"><span class="fs-4 fw-bold">php {i['price']}</span>
                    </div>
                    <button class="btn btn-primary w-100 rounded-pill" id="add-to-cart-btn" class="position-relative"
                    data-bs-toggle="modal" data-bs-target="#itemviewmodal">view</button>
                </div>
                <div>
                    <input type="hidden" name="category" value="{i['category']}">
                    <input type="hidden" name="section" value="{i['section']}">
                </div>
                </div>
            </div>\n"""
        return data

# Additional routes can be added here following the same pattern