from flask import jsonify, request, render_template, redirect, url_for
import json
import math
from database import get_db, get_db_connection, get_all_products
from pagination import current_page, filterz, total_pagez, generate_pagination_links

def init_shop_routes(app):
    @app.route("/shop")
    @app.route("/shop/<int:page>", methods=['GET', 'POST'])
    def shop(page=1):
        per_page = 20
        page = int(request.args.get('page', page))
        if not request.args.get('page'):
            filterz.set_current_filters([])
        current_page.set_current_page(page)

        if page > total_pagez.get_total_pages() and total_pagez.get_total_pages() != 0:
            return redirect(url_for('shop'))

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

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({
                'products': processed_products,
                'cart': cart,
                'cart_len': len(cart),
                'current_page': page,
                'total_pages': total_pagez.get_total_pages()
            })

        pagination_links = generate_pagination_links(page, total_pagez.get_total_pages())

        if filterz.get_current_filters():
            return render_template(
                "menu.html",
                products=processed_products,
                cart=cart,
                cart_len=len(cart),
                current_page=page,
                total_pages=total_pagez.get_total_pages(),
                filters=list(set(filterz.get_current_filters())),
                pagination_links=pagination_links
            )
        else:
            return render_template(
                "menu.html",
                products=processed_products,
                cart=cart,
                cart_len=len(cart),
                current_page=page,
                total_pages=total_pagez.get_total_pages(),
                pagination_links=pagination_links,
            )

    @app.route("/api/shop_data", methods=['GET', 'POST'])
    def api_shop_data():
        try:
            page = int(request.args.get('page', 1))
            per_page = 20
            offset = (page - 1) * per_page

            if not request.args.get('page'):
                filterz.set_current_filters = []

            conn = get_db('ecommerce.db')
            cursor = conn.cursor()

            query = '''
                SELECT product_id, name, price, images, section, category, data
                FROM products
            '''
            params = []

            categories_param = filterz.get_current_filters()

            if categories_param:
                try:
                    selected_categories = filterz.get_current_filters()
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
            print(f"Error fetching shop data: {e}")
            return jsonify({'error': 'Failed to fetch shop data'}), 500