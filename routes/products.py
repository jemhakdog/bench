from flask import jsonify, request, render_template, redirect, url_for
import json
from database import get_db, get_db_connection, get_all_products, get_existing_image_path
from pagination import current_page, filterz, total_pagez, generate_pagination_links
from werkzeug.utils import secure_filename
import os

def init_product_routes(app):
    @app.route("/products")
    @app.route("/products/<int:page>", methods=['GET', 'POST'])
    def products_route(page=1):
        per_page = 20
        page = int(request.args.get('page', page))
        current_page.set_current_page(page)

        conn = get_db('ecommerce.db')
        cursor = conn.cursor()

        query = '''
            SELECT product_id, name, price, images, section, category, data
            FROM products
        '''
        params = []

        if request.method == 'POST' and request.is_json or filterz.get_current_filters():
            if filterz.get_current_filters():
                filters = filterz.get_current_filters()
            else:
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

        offset = (page - 1) * per_page
        query += ' LIMIT ? OFFSET ?'
        params.extend([per_page, offset])

        cursor.execute(query, params)
        products = cursor.fetchall()

        cart_conn = get_db_connection()
        cart_cursor = cart_conn.cursor()
        cart_cursor.execute('SELECT * FROM cart')
        cart_items = cart_cursor.fetchall()
        cart_conn.close()
        cart = [dict(item) for item in cart_items]

        processed_products = []
        total_pagez.set_total_pages(int(len(get_all_products())/20))

        for product in products:
            product_dict = dict(product)
            product_dict['images'] = json.loads(product_dict['images'])
            product_dict['data'] = json.loads(product_dict['data'])
            processed_products.append(product_dict)

        conn.close()
        return jsonify({"len": len(processed_products), "product": processed_products})

    @app.route('/products/add', methods=['GET', 'POST'])
    def add_product():
        if request.method == 'POST':
            name = request.form['name']
            price = request.form['price']
            category = request.form['category']
            section = request.form.get('section', '')
            images = []

            if 'images' in request.files:
                image_files = request.files.getlist('images')
                for image in image_files:
                    if image:
                        image_filename = secure_filename(image.filename)
                        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
                        image.save(image_path)
                        images.append(image_filename)

            images_json = json.dumps(images)

            conn = get_db('ecommerce.db')
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO products (product_id, name, link, price, images, section, category)
                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (None, name, '', price, images_json, section, category))
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
            image = request.files['image']
            category = request.form['category']

            if image:
                upload_folder = 'static/images'
                filename = secure_filename(image.filename)
                image_path = os.path.join(upload_folder, filename)
                image.save(image_path)
                image = image_path
            else:
                image = get_existing_image_path(id)

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

    @app.route('/api/products')
    def api_products():
        products = get_all_products()
        for product in products:
            product['images'] = json.loads(product['images'])
            product['data'] = product['data']
        return jsonify(products)