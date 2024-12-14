import math
from flask import *
from werkzeug.utils import secure_filename

import sqlite3

import os
app = Flask(__name__, static_url_path="", static_folder="static", template_folder="templates")

DATABASE = 'ecommerce.db'
from datetime import datetime
from typing import List, Dict, Any


# def generate_pagination_links(current_page, total_pages, page_range=5):
#     pagination_links = ""
#     start_page = max(1, current_page - (page_range // 2))
#     end_page = min(total_pages, start_page + page_range - 1)

#     # Adjust start_page if at the end of range
#     if end_page - start_page < page_range - 1:
#         start_page = max(1, end_page - page_range + 1)

#     # Previous button
#     # if current_page > 1:
#         # pagination_links += f"<li class='page-item'><a class='page-link' href='?page={current_page - 1}'>Previous</a></li>"

#     # Page links
#     for p in range(start_page, end_page + 1):
#         if p == current_page:
#             pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
#         else:
#             pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"

#     # Next button
#     # if current_page < total_pages:
#         # pagination_links += f"<li class='page-item'><a class='page-link' href='?page={current_page + 1}'>Next</a></li>"

#     # Current page of total pages
#     pagination_links += f"<li class='page-item disabled'><span class='page-link'>Page {current_page} of {total_pages}</span></li>"

#     return pagination_links

def generate_pagination_links(current_page, total_pages):
    pagination_links = ""
    print("generate_pagination_links:",current_page,total_pages)

    start_page = max(1, current_page - (5 // 2))
    end_page = min(total_pages, start_page + 5 - 1)
    # Adjust start_page if at the end of range
    if end_page - start_page < 5 - 1:
        start_page = max(1, end_page - 5 + 1)

    # Previous button
    if current_page > 1:
        pagination_links += f"<li class='page-item'><a class='page-link' href='?page={current_page - 1}'>Previous</a></li>"

    # Page links
    for p in range(start_page, end_page + 1):
        if p == current_page:
            pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
        else:
            pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"

    # Next button
    if current_page < total_pages:
        pagination_links += f"<li class='page-item'><a class='page-link' href='?page={current_page + 1}'>Next</a></li>"

    # Jump to page select


    # Current page of total pages
    pagination_links += f"<li class='page-item disabled'><span class='page-link'>Page {current_page} of {total_pages}</span></li>"
    pagination_links += f"""
        <li class='page-item'>
        <select class='page-link form-select' aria-label='Jump to' onchange='window.location.href = "?page=" + (this.value === "jump to" ? 1 : this.value)' >
            <option value='1' selected>jump to</option>
                {"".join(f"<option value='{p}' {'selected' if p == current_page else ''}>{p}</option>" for p in range(1, total_pages + 1))}
            </select>
        </li>
    """
    return pagination_links


class Page:
    def __init__(self):
        self.current_page = 1
    def set_current_page(self, current_page):
        self.current_page = current_page
    def get_current_page(self):
        return self.current_page
    
class Filters:
    def __init__(self):
        self.filters = []
    def set_current_filters(self, filters):
        self.filters = filters
    def get_current_filters(self):
        return self.filters

class TotalPages:
    def __init__(self):
        self.total_pages = 0
    def set_total_pages(self, total_pages):
        self.total_pages = total_pages
    def get_total_pages(self):
        return self.total_pages

class Pagination:
    def __init__(self, page: Page, total_pages: TotalPages, filters: Filters):
        self._page = page
        self._total_pages = total_pages
        self._filters = filters

    def get_page(self) -> Page:
        return self._page

    def set_page(self, page: Page):
        self._page = page

    def get_total_pages(self) -> TotalPages:
        return self._total_pages

    def set_total_pages(self, total_pages: TotalPages):
        self._total_pages = total_pages

    def get_filters(self) -> Filters:
        return self._filters

    def set_filters(self, filters: Filters):
        self._filters = filters

    def get_paginations(self):
        # You can implement the logic for get_paginations here
        pass
            
        

current_page=Page()
filterz=Filters()
total_pagez=TotalPages()
pagination = Pagination(None,None,None)
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


# @app.route("/pagination", methods=['GET', 'POST'])
# def pagination():
#     if request.method == 'POST':
#         page=current_page.get_current_page()
#         data = request.get_json()
#         try:
#             min=request.form['min']
#             max=request.form['max']

#         except:
#             min=None
#             max=None

#         # Get database connection
#         conn = get_db('ecommerce.db')
#         cursor = conn.cursor()

#         # Base query
#         query = '''
#             SELECT product_id, name, price, images, section, category, data
#             FROM products
#         '''
#         params = []

#         # Add filters if present
#         if data and 'categories' in data:
#             selected_filters = data.get('categories', [])
#             if selected_filters:
#                 filter_conditions = []

#                 for filter_id in selected_filters:
#                     clean_filter = filter_id
#                     for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                         if clean_filter.startswith(prefix):
#                             the_category = clean_filter.replace(prefix, '')
#                             the_section = prefix[:-1]

#                             filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
#                             params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

#                 if filter_conditions:
#                     query += ' WHERE ' + ' OR '.join(filter_conditions)

#         # Add price range filter if present
#         if min and max:
#             query += ' WHERE price BETWEEN ? AND ?'
#             params.append(min)
#             params.append(max)

#         # Execute query
#         cursor.execute(query, params)
#         products = cursor.fetchall()
#         data=""

#         pagination_links = generate_pagination_links(page, total_pages)

#         # pagination_links = ""
#         # if total_pagez.get_total_pages() >= 1:
#         #     for p in range(1,  total_pagez.get_total_pages() + 1):
#         #         if p == current_page.get_current_page():
#         #             pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
#         #         else:
#         #             pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"
#         # else:

#         #     for p in range(1,  58 + 1):
#         #         if p == current_page.get_current_page():
#         #             pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
#         #         else:
#         #             pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"

#         print("current pagination links:",pagination_links)
#         return   pagination_links

        # if not products:
        #     return jsonify({'total_pages':0})

        # pagi = math.ceil(len(products)/20)
        # total_pagez.set_total_pages(pagi)


        # return jsonify({'total_pages':pagi,'current_page':current_page.get_current_page(),'filters':filterz.get_current_filters()})


@app.route("/pagination", methods=['GET', 'POST'])
def pagination():
    if request.method == 'POST':

        # Get the current page from the URL query string
        page = request.args.get('page', 1, type=int)
        print("calling pagination from post:",page)

        current_page.set_current_page(page)

        data = request.get_json()
        try:
            min=request.form['min']
            max=request.form['max']

        except:
            min=None
            max=None

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
                        if clean_filter.startswith(prefix):
                            the_category = clean_filter.replace(prefix, '')
                            the_section = prefix[:-1]

                            filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
                            params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

                if filter_conditions:
                    query += ' WHERE ' + ' OR '.join(filter_conditions)

        # Add price range filter if present
        if min and max:
            query += ' WHERE price BETWEEN ? AND ?'
            params.append(min)
            params.append(max)

        # Execute query
        cursor.execute(query, params)
        products = cursor.fetchall()

        processed_products = []
        for product in products:
            product_dict = dict(product)
            # Safely parse JSON fields
            try:
                product_dict['images'] = json.loads(product_dict['images'])
            except json.JSONDecodeError:
                product_dict['images'] = []

            processed_products.append(product_dict)

        # Calculate total pages
        per_page = 20
        total_pages = math.ceil(len(products)/per_page)



        # Count total products after filtering
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
# @app.route("/pagination", methods=['GET', 'POST'])
# def pagination():
#     if request.method == 'POST':
#         page=current_page.get_current_page()
#         data = request.get_json()
#         try:
#             min=request.form['min']
#             max=request.form['max']

#         except:
#             min=None
#             max=None

#         # Get database connection
#         conn = get_db('ecommerce.db')
#         cursor = conn.cursor()

#         # Base query
#         query = '''
#             SELECT product_id, name, price, images, section, category, data
#             FROM products
#         '''
#         params = []

#         # Add filters if present
#         if data and 'categories' in data:
#             selected_filters = data.get('categories', [])
#             if selected_filters:
#                 filter_conditions = []

#                 for filter_id in selected_filters:
#                     clean_filter = filter_id
#                     for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                         if clean_filter.startswith(prefix):
#                             the_category = clean_filter.replace(prefix, '')
#                             the_section = prefix[:-1]

#                             filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
#                             params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

#                 if filter_conditions:
#                     query += ' WHERE ' + ' OR '.join(filter_conditions)

#         # Add price range filter if present
#         if min and max:
#             query += ' WHERE price BETWEEN ? AND ?'
#             params.append(min)
#             params.append(max)

#         # Execute query
#         cursor.execute(query, params)
#         products = cursor.fetchall()

#         # Calculate total pages
#         per_page = 20
#         total_pages = math.ceil(len(products)/per_page)

#         # Generate pagination links
#         pagination_links = generate_pagination_links(current_page.get_current_page(), total_pages)

#         return pagination_links

        # if not products:
        #     return jsonify({'total_pages':0})

        # pagi = math.ceil(len(products)/20)
        # total_pagez.set_total_pages(pagi)


        # return jsonify({'total_pages':pagi,'current_page':current_page.get_current_page(),'filters':filterz.get_current_filters()})

# @app.route("/filter", methods=['GET', 'POST'])
# def filter():
#     if request.method == 'POST':
#         data = request.get_json()

#         filterz.set_current_filters(data.get('categories'))
#         try:
#             min=request.form['min']
#             max=request.form['max']
#         except:
#             min=None
#             max=None

#         # Get database connection
#         conn = get_db('ecommerce.db')
#         cursor = conn.cursor()

#         # Base query
#         query = '''
#             SELECT product_id, name, price, images, section, category, data
#             FROM products
#         '''
#         params = []

#         # Add filters if present
#         if data and 'categories' in data:
#             selected_filters = data.get('categories', [])
#             if selected_filters:
#                 filter_conditions = []

#                 for filter_id in selected_filters:
#                     clean_filter = filter_id
#                     for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                         if clean_filter.startswith(prefix):
#                             the_category = clean_filter.replace(prefix, '')
#                             the_section = prefix[:-1]

#                             filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
#                             params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

#                 if filter_conditions:
#                     query += ' WHERE ' + ' OR '.join(filter_conditions)

#         # Add price range filter if present
#         if min and max:
#             if 'WHERE' in query:
#                 query += ' AND price BETWEEN ? AND ?'
#             else:
#                 query += ' WHERE price BETWEEN ? AND ?'
#             params.append(min)
#             params.append(max)

#         # Execute query to get total count
#         cursor.execute(query, params)
#         total = len(cursor.fetchall())

#         # Calculate total pages
#         per_page = 20
#         total_pages = (total + per_page - 1) // per_page

#         total_pagez.set_total_pages(total_pages)


#         # Get current page
#         page = request.args.get('page', 1, type=int)

#         # Calculate offset
#         offset = (page - 1) * per_page

#         # Add pagination to query
#         query += ' LIMIT ? OFFSET ?'
#         params.extend([per_page, offset])

#         # Execute query with pagination
#         cursor.execute(query, params)
#         products = cursor.fetchall()

#         data=""
#         if not products:
#             return "<h5>no products found!</h5>"

#         for i in products:
#             thedata = json.loads(i['data'])
#             data+=f"""<div class="col-lg-4 product-item" id="{ i['product_id'] } { i['section']}-{ i['category']}">
#                 <div class="card border-0 shadow-sm rounded-3 mb-3">
#                 <!-- <img class="card-img-top w-100 d-block card-img-top rounded-top-3" src="{json.loads(i['images'])[0]}" alt="Product Image"> -->
#                 <!-- Main product image -->
#                 <img class="card-img-top w-100 d-block card-img-top rounded-top-3" src="{json.loads(i['images'])[0]}"
#                     alt="Product Image" id="main-image"
#                     onclick="window.location.href = `/product/view/{ i['product_id'] }`">

#                 <!-- Hover image for the same product -->
#                 <img class="card-img-top w-100 d-block card-img-top rounded-top-3 card-img-hover"
#                     src="{ json.loads(i['images'])[1] }" alt="Product Image Hover" id="hover-image"
#                     onclick="window.location.href = `/product/view/{ i['product_id'] }`">

#                 <div class="card-body">
#                     <h5 class="fw-bold card-title mb-2">{ i['name'] }</h5>
#                     <div class="d-flex justify-content-between align-items-center mb-3"><span class="fs-4 fw-bold">php { i['price'] }</span>
#                     <!-- <div class="input-group input-group-sm" style="width:120px;"><button class="btn btn-outline-secondary"
#                         type="button" id="decrease-quantity">-</button><input
#                         class="form-control form-control text-center" type="number" id="quantity-input" min="1"
#                         value="1"><button class="btn btn-outline-secondary" type="button"
#                         id="increase-quantity">+</button>
#                     </div> -->
#                     <div class="input-group input-group-sm" style="width: 120px">
#                         <button
#                         class="btn btn-outline-secondary"
#                         type="button"
#                         onclick="updateQuantity(-1)"
#                         >
#                         -
#                         </button>
#                         <input
#                         class="form-control form-control text-center"
#                         type="number"
#                         id="productQuantity"
#                         name="productQuantity"
#                         min="1"
#                         value="1"
#                         />
#                         <button
#                         class="btn btn-outline-secondary"
#                         type="button"
#                         onclick="updateQuantity(1)"
#                         >
#                         +
#                         </button>
#                     </div>
#                     </div><button class="btn btn-primary w-100 rounded-pill" id="add-to-cart-btn" class="position-relative"
#                     data-bs-toggle="modal" data-bs-target="#itemviewmodal">Add to Cart</button>
#                 </div>
#                 <div>
#                     <input type="hidden" name="category" value="{ i['category'] }">
#                     <input type="hidden" name="section" value="{ i['section'] }">
#                 </div>
#                 </div>
#             </div>\n"""
#         pagination_links = ""
#         if total_pages > 1:
#             for p in range(1, total_pages + 1):
#                 if p == current_page.get_current_page():
#                     pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
#                 else:
#                     pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"
#         return data + "<ul class='pagination'>" + pagination_links + "</ul>"


@app.route("/filter", methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        data = request.get_json()

        filterz.set_current_filters(data.get('categories'))
        try:
            min=request.form['min']
            max=request.form['max']
        except:
            min=None
            max=None

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
                        if clean_filter.startswith(prefix):
                            the_category = clean_filter.replace(prefix, '')
                            the_section = prefix[:-1]

                            filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
                            params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

                if filter_conditions:
                    query += ' WHERE ' + ' OR '.join(filter_conditions)

        # Add price range filter if present
        if min and max:
            if 'WHERE' in query:
                query += ' AND price BETWEEN ? AND ?'
            else:
                query += ' WHERE price BETWEEN ? AND ?'
            params.append(min)
            params.append(max)

        # Execute query to get total count
        cursor.execute(query, params)
        total = len(cursor.fetchall())

        # Calculate total pages
        per_page = 20
        total_pages = (total + per_page - 1) // per_page
        print("filter is setting total pages to:",total_pages)
        total_pagez.set_total_pages(total_pages)



        # Get current page
        page = request.args.get('page', 1, type=int)

        # Calculate offset
        offset = (page - 1) * per_page

        # Add pagination to query
        query += ' LIMIT ? OFFSET ?'
        params.extend([per_page, offset])

        # Execute query with pagination
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
                    style="height: 401px;"
                    onclick="window.location.href = `/product/view/{ i['product_id'] }`">

                <!-- Hover image for the same product -->
                <img class="card-img-top w-100 d-block card-img-top rounded-top-3 card-img-hover"
                    src="{ json.loads(i['images'])[1] }" alt="Product Image Hover" id="hover-image"
                       style="height: 401px;"
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

                    </div><button class="btn btn-primary w-100 rounded-pill" id="add-to-cart-btn" class="position-relative"
                    data-bs-toggle="modal" data-bs-target="#itemviewmodal">view</button>
                </div>
                <div>
                    <input type="hidden" name="category" value="{ i['category'] }">
                    <input type="hidden" name="section" value="{ i['section'] }">
                </div>
                </div>
            </div>\n"""
        # pagination_links = ""
        # if total_pagez.get_total_pages() > 1:
        #     for p in range(1, total_pagez.get_total_pages() + 1):
        #         if p == current_page.get_current_page():
        #             pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
        #         else:
        #             pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"
        return data
# # @app.route("/filter", methods=['GET', 'POST'])
# def filter():
#     if request.method == 'POST':
#         data = request.get_json()

#         filterz.set_current_filters(data.get('categories'))
#         try:
#             min=request.form['min']
#             max=request.form['max']
#         except:
#             min=None
#             max=None

#         # Get database connection
#         conn = get_db('ecommerce.db')
#         cursor = conn.cursor()

#         # Base query
#         query = '''
#             SELECT product_id, name, price, images, section, category, data
#             FROM products
#         '''
#         params = []

#         # Add filters if present
#         if data and 'categories' in data:
#             selected_filters = data.get('categories', [])
#             if selected_filters:
#                 filter_conditions = []

#                 for filter_id in selected_filters:
#                     clean_filter = filter_id
#                     for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                         if clean_filter.startswith(prefix):
#                             the_category = clean_filter.replace(prefix, '')
#                             the_section = prefix[:-1]

#                             filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
#                             params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

#                 if filter_conditions:
#                     query += ' WHERE ' + ' OR '.join(filter_conditions)

#         # Add price range filter if present
#         if min and max:
#             query += ' WHERE price BETWEEN ? AND ?'
#             params.append(min)
#             params.append(max)
#         query+=' LIMIT 20'

#         # Execute query
#         cursor.execute(query, params)
#         products = cursor.fetchall()

#         data=""
#         if not products:
#             return "<h5>no products found!</h5>"

#         for i in products:
#             thedata = json.loads(i['data'])
#             data+=f"""<div class="col-lg-4 product-item" id="{ i['product_id'] } { i['section']}-{ i['category']}">
#                 <div class="card border-0 shadow-sm rounded-3 mb-3">
#                 <!-- <img class="card-img-top w-100 d-block card-img-top rounded-top-3" src="{json.loads(i['images'])[0]}" alt="Product Image"> -->
#                 <!-- Main product image -->
#                 <img class="card-img-top w-100 d-block card-img-top rounded-top-3" src="{json.loads(i['images'])[0]}"
#                     alt="Product Image" id="main-image"
#                     onclick="window.location.href = `/product/view/{ i['product_id'] }`">

#                 <!-- Hover image for the same product -->
#                 <img class="card-img-top w-100 d-block card-img-top rounded-top-3 card-img-hover"
#                     src="{ json.loads(i['images'])[1] }" alt="Product Image Hover" id="hover-image"
#                     onclick="window.location.href = `/product/view/{ i['product_id'] }`">

#                 <div class="card-body">
#                     <h5 class="fw-bold card-title mb-2">{ i['name'] }</h5>
#                     <div class="d-flex justify-content-between align-items-center mb-3"><span class="fs-4 fw-bold">php { i['price'] }</span>
#                     <!-- <div class="input-group input-group-sm" style="width:120px;"><button class="btn btn-outline-secondary"
#                         type="button" id="decrease-quantity">-</button><input
#                         class="form-control form-control text-center" type="number" id="quantity-input" min="1"
#                         value="1"><button class="btn btn-outline-secondary" type="button"
#                         id="increase-quantity">+</button>
#                     </div> -->
#                     <div class="input-group input-group-sm" style="width: 120px">
#                         <button
#                         class="btn btn-outline-secondary"
#                         type="button"
#                         onclick="updateQuantity(-1)"
#                         >
#                         -
#                         </button>
#                         <input
#                         class="form-control form-control text-center"
#                         type="number"
#                         id="productQuantity"
#                         name="productQuantity"
#                         min="1"
#                         value="1"
#                         />
#                         <button
#                         class="btn btn-outline-secondary"
#                         type="button"
#                         onclick="updateQuantity(1)"
#                         >
#                         +
#                         </button>
#                     </div>
#                     </div><button class="btn btn-primary w-100 rounded-pill" id="add-to-cart-btn" class="position-relative"
#                     data-bs-toggle="modal" data-bs-target="#itemviewmodal">Add to Cart</button>
#                 </div>
#                 <div>
#                     <input type="hidden" name="category" value="{ i['category'] }">
#                     <input type="hidden" name="section" value="{ i['section'] }">
#                 </div>
#                 </div>
#             </div>\n"""
#         return data

# @app.route("/shop")
# @app.route("/shop/<int:page>", methods=['GET', 'POST'])
# def shop(page=1):
#     per_page = 20
#     current_page.set_current_page(page)
#     if page > total_pagez.get_total_pages() and total_pagez.get_total_pages()!=0:
#         return redirect(url_for('shop', page=1))

#     # Get database connection
#     conn = get_db('ecommerce.db')
#     cursor = conn.cursor()

#     # Get total count for pagination
#     cursor.execute('SELECT COUNT(*) FROM products')
#     total = cursor.fetchone()[0]
#     total_pages = (total + per_page - 1) // per_page
#     page = min(max(1, page), total_pages)
#     offset = (page - 1) * per_page

#     # Base query
#     query = '''
#         SELECT product_id, name, price, images, section, category, data
#         FROM products
#     '''
#     params = []


#     # Handle filters if present
#     if request.method == 'POST' and request.is_json or filterz.get_current_filters():
#         if filterz.get_current_filters():
#             filters = filterz.get_current_filters()
#         else:
#             filters = request.get('categories', [])


#         if filters:
#             filter_conditions = []
#             for filter_id in filters:
#                 clean_filter = filter_id
#                 for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                     if clean_filter.startswith(prefix):
#                         the_category = clean_filter.replace(prefix, '')
#                         the_section = prefix[:-1]
#                         filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
#                         params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

#                 # for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                 #     clean_filter = clean_filter.replace(prefix, '')
#                 # clean_filter = clean_filter.replace('-', ' ')
#                 # filter_conditions.append('(LOWER(section) LIKE ? OR LOWER(category) LIKE ?)')
#                 # params.extend([f'%{clean_filter.lower()}%', f'%{clean_filter.lower()}%'])

#             if filter_conditions:
#                 query += ' WHERE ' + ' OR '.join(filter_conditions)

#     # Add pagination
#     query += ' LIMIT ? OFFSET ?'
#     params.extend([per_page, offset])

#     # Execute final query
#     cursor.execute(query, params)
#     products = cursor.fetchall()

#     # Get cart items
#     cart_conn = get_db_connection()
#     cart_cursor = cart_conn.cursor()
#     cart_cursor.execute('SELECT * FROM cart')
#     cart_items = cart_cursor.fetchall()
#     cart_conn.close()
#     cart = [dict(item) for item in cart_items]

#     # Process products
#     processed_products = []
#     for product in products:
#         product_dict = dict(product)
#         product_dict['images'] = json.loads(product_dict['images'])
#         product_dict['data'] = json.loads(product_dict['data'])
#         processed_products.append(product_dict)

#     conn.close()

#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         return jsonify({
#             'products': processed_products,
#             'cart': cart,
#             'cart_len': len(cart),
#             'current_page': page,
#             'total_pages': total_pages
#         })
#     pagination_links = ""
#     if total_pagez.get_total_pages() > 1:
#         for p in range(1, total_pagez.get_total_pages() + 1):
#             if p == current_page.get_current_page():
#                 pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
#             else:
#                 pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"
#     print(total_pages,total_pagez.get_total_pages())

#     if filterz.get_current_filters():
#         return render_template(
#             "menu.html",
#             products=processed_products,
#             cart=cart,
#             cart_len=len(cart),
#             current_page=page,
#             total_pages=total_pages,
#             filters=list(set(filterz.get_current_filters())),
#             pagination_links=pagination_links
#         )
#     else:
#         return render_template(
#             "menu.html",
#             products=processed_products,
#             cart=cart,
#             cart_len=len(cart),
#             current_page=page,
#             total_pages=total_pages,
#             pagination_links=pagination_links,
#         )
    # return render_template(
    #     "menu.html",
    #     products=processed_products,
    #     cart=cart,
    #     cart_len=len(cart),
    #     current_page=page,
    #     total_pages=total_pages,
#     # )
# @app.route("/shop")
# @app.route("/shop/<int:page>", methods=['GET', 'POST'])
# def shop(page=1):
#     per_page = 20
#     current_page.set_current_page(page)
#     if page > total_pagez.get_total_pages() and total_pagez.get_total_pages()!=0:
#         return redirect(url_for('shop', page=1))

#     # Get database connection
#     conn = get_db('ecommerce.db')
#     cursor = conn.cursor()

#     # Get total count for pagination
#     cursor.execute('SELECT COUNT(*) FROM products')
#     total = cursor.fetchone()[0]
#     total_pages = (total + per_page - 1) // per_page
#     page = min(max(1, page), total_pages)
#     offset = (page - 1) * per_page

#     # Base query
#     query = '''
#         SELECT product_id, name, price, images, section, category, data
#         FROM products
#     '''
#     params = []


#     # Handle filters if present
#     if request.method == 'POST' and request.is_json or filterz.get_current_filters():
#         if filterz.get_current_filters():
#             filters = filterz.get_current_filters()
#         else:
#             filters = request.get('categories', [])


#         if filters:
#             filter_conditions = []
#             for filter_id in filters:
#                 clean_filter = filter_id
#                 for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                     if clean_filter.startswith(prefix):
#                         the_category = clean_filter.replace(prefix, '')
#                         the_section = prefix[:-1]
#                         filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
#                         params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

#                 # for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                 #     clean_filter = clean_filter.replace(prefix, '')
#                 # clean_filter = clean_filter.replace('-', ' ')
#                 # filter_conditions.append('(LOWER(section) LIKE ? OR LOWER(category) LIKE ?)')
#                 # params.extend([f'%{clean_filter.lower()}%', f'%{clean_filter.lower()}%'])

#             if filter_conditions:
#                 query += ' WHERE ' + ' OR '.join(filter_conditions)

#     # Add pagination
#     query += ' LIMIT ? OFFSET ?'
#     params.extend([per_page, offset])

#     # Execute final query
#     cursor.execute(query, params)
#     products = cursor.fetchall()

#     # Get cart items
#     cart_conn = get_db_connection()
#     cart_cursor = cart_conn.cursor()
#     cart_cursor.execute('SELECT * FROM cart')
#     cart_items = cart_cursor.fetchall()
#     cart_conn.close()
#     cart = [dict(item) for item in cart_items]

#     # Process products
#     processed_products = []
#     for product in products:
#         product_dict = dict(product)
#         product_dict['images'] = json.loads(product_dict['images'])
#         product_dict['data'] = json.loads(product_dict['data'])
#         processed_products.append(product_dict)

#     conn.close()

#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         return jsonify({
#             'products': processed_products,
#             'cart': cart,
#             'cart_len': len(cart),
#             'current_page': page,
#             'total_pages': total_pages
#         })
#     pagination_links = ""
#     if total_pagez.get_total_pages() > 1:
#         for p in range(1, total_pagez.get_total_pages() + 1):
#             if p == current_page.get_current_page():
#                 pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
#             else:
#                 pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"
#     else:
#         for p in range(1, 58 + 1):
#             if p == current_page.get_current_page():
#                 pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
#             else:
#                 pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"

#     print(total_pages,total_pagez.get_total_pages())

#     if filterz.get_current_filters():
#         return render_template(
#             "menu.html",
#             products=processed_products,
#             cart=cart,
#             cart_len=len(cart),
#             current_page=page,
#             total_pages=total_pages,
#             filters=list(set(filterz.get_current_filters())),
#             pagination_links=pagination_links
#         )
#     else:
#         return render_template(
#             "menu.html",
#             products=processed_products,
#             cart=cart,
#             cart_len=len(cart),
#             current_page=page,
#             total_pages=total_pages,
#             pagination_links=pagination_links,
#         )
# @app.route("/shop")
# @app.route("/shop/<int:page>", methods=['GET', 'POST'])
# def shop(page=1):
#     per_page = 20
#     current_page.set_current_page(page)
#     page = int(request.args.get('page', 1))
#     print("total pages in shop are:",total_pagez.get_total_pages())

#     if page > total_pagez.get_total_pages() and total_pagez.get_total_pages()!=0:
#         return redirect(url_for('shop'))

#     # Get database connection
#     conn = get_db('ecommerce.db')
#     cursor = conn.cursor()

#     # Get total count for pagination
#     cursor.execute('SELECT COUNT(*) FROM products')
#     total = cursor.fetchone()[0]
#     total_pages = (total + per_page - 1) // per_page
#     # total_pagez.set_total_pages(total_pages) # Set total pages here

#     page = min(max(1, page), total_pages)
#     offset = (page - 1) * per_page
#     print("page and offset:",page,offset)

#     # Base query
#     query = '''
#         SELECT product_id, name, price, images, section, category, data
#         FROM products
#     '''
#     params = []


#     # Handle filters if present
#     if request.method == 'POST' and request.is_json or filterz.get_current_filters():
#         if filterz.get_current_filters():
#             filters = filterz.get_current_filters()
#         else:
#             filters = request.get('categories', [])


#         if filters:
#             filter_conditions = []
#             for filter_id in filters:
#                 clean_filter = filter_id
#                 for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                     if clean_filter.startswith(prefix):
#                         the_category = clean_filter.replace(prefix, '')
#                         the_section = prefix[:-1]
#                         filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
#                         params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

#                 # for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                 #     clean_filter = clean_filter.replace(prefix, '')
#                 # clean_filter = clean_filter.replace('-', ' ')
#                 # filter_conditions.append('(LOWER(section) LIKE ? OR LOWER(category) LIKE ?)')
#                 # params.extend([f'%{clean_filter.lower()}%', f'%{clean_filter.lower()}%'])

#             if filter_conditions:
#                 query += ' WHERE ' + ' OR '.join(filter_conditions)

#     # Add pagination
#     query += ' LIMIT ? OFFSET ?'
#     params.extend([per_page, offset])

#     # Execute final query
#     cursor.execute(query, params)
#     products = cursor.fetchall()
#     print("len of proucts:",len(products))
#     # Get cart items
#     cart_conn = get_db_connection()
#     cart_cursor = cart_conn.cursor()
#     cart_cursor.execute('SELECT * FROM cart')
#     cart_items = cart_cursor.fetchall()
#     cart_conn.close()
#     cart = [dict(item) for item in cart_items]

#     # Process products
#     processed_products = []
#     for product in products:
#         product_dict = dict(product)
#         product_dict['images'] = json.loads(product_dict['images'])
#         product_dict['data'] = json.loads(product_dict['data'])
#         processed_products.append(product_dict)

#     conn.close()

#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         return jsonify({
#             'products': processed_products,
#             'cart': cart,
#             'cart_len': len(cart),
#             'current_page': page,
#             'total_pages': total_pages
#         })
#     pagination_links = generate_pagination_links(page, total_pagez.get_total_pages())

#     # if total_pagez.get_total_pages() > 1:
#     #         for p in range(1, total_pagez.get_total_pages() + 1):
#     #             if p == page:
#     #                 pagination_links += f"<li class='page-item active'><a class='page-link' href='?page={p}'>{p}</a></li>"
#     #             else:
#     #                 pagination_links += f"<li class='page-item'><a class='page-link' href='?page={p}'>{p}</a></li>"


#     if filterz.get_current_filters():
#         return render_template(
#             "menu.html",
#             products=processed_products,
#             cart=cart,
#             cart_len=len(cart),
#             current_page=page,
#             total_pages=total_pages,
#             filters=list(set(filterz.get_current_filters())),
#             pagination_links=pagination_links
#         )
#     else:
#         return render_template(
#             "menu.html",
#             products=processed_products,
#             cart=cart,
#             cart_len=len(cart),
#             current_page=page,
#             total_pages=total_pages,
#             pagination_links=pagination_links,
#         )


# almost working
# @app.route("/shop")
# @app.route("/shop/<int:page>", methods=['GET', 'POST'])
# def shop(page=1):
#     per_page = 20
#     page = int(request.args.get('page', page))
#     current_page.set_current_page(page)


#     if page > total_pagez.get_total_pages() and total_pagez.get_total_pages() != 0:
#         return redirect(url_for('shop'))

#     # Get database connection
#     conn = get_db('ecommerce.db')
#     cursor = conn.cursor()

#     # Get total count for pagination
#     cursor.execute('SELECT COUNT(*) FROM products')
#     total = cursor.fetchone()[0]
#     total_pages = (total + per_page - 1) // per_page

#     page = int(request.args.get('page', page))
#     print("page found:",page)
#     current_page.set_current_page(page)
#     offset = (page - 1) * per_page

#     # Base query
#     query = '''
#         SELECT product_id, name, price, images, section, category, data
#         FROM products
#     '''
#     params = []

#     # Handle filters if present
#     if request.method == 'POST' and request.is_json or filterz.get_current_filters():
#         if filterz.get_current_filters():
#             filters = filterz.get_current_filters()
#         else:
#             filters = request.get('categories', [])

#         if filters:
#             filter_conditions = []
#             for filter_id in filters:
#                 clean_filter = filter_id
#                 for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                     if clean_filter.startswith(prefix):
#                         the_category = clean_filter.replace(prefix, '')
#                         the_section = prefix[:-1]
#                         filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
#                         params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

#             if filter_conditions:
#                 query += ' WHERE ' + ' OR '.join(filter_conditions)

#     # Add pagination
#     query += ' LIMIT ? OFFSET ?'
#     params.extend([per_page, offset])

#     # Execute final query
#     cursor.execute(query, params)
#     products = cursor.fetchall()

#     # Get cart items
#     cart_conn = get_db_connection()
#     cart_cursor = cart_conn.cursor()
#     cart_cursor.execute('SELECT * FROM cart')
#     cart_items = cart_cursor.fetchall()
#     cart_conn.close()
#     cart = [dict(item) for item in cart_items]

#     # Process products
#     processed_products = []
#     for product in products:
#         product_dict = dict(product)
#         product_dict['images'] = json.loads(product_dict['images'])
#         product_dict['data'] = json.loads(product_dict['data'])
#         processed_products.append(product_dict)

#     conn.close()

#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         return jsonify({
#             'products': processed_products,
#             'cart': cart,
#             'cart_len': len(cart),
#             'current_page': page,
#             'total_pages': total_pages
#         })
#     print("calling paginator:",page)
#     # Generate pagination links
#     pagination_links = generate_pagination_links(page, total_pages)

#     if filterz.get_current_filters():
#         return render_template(
#             "menu.html",
#             products=processed_products,
#             cart=cart,
#             cart_len=len(cart),
#             current_page=page,
#             total_pages=total_pages,
#             filters=list(set(filterz.get_current_filters())),
#             pagination_links=pagination_links
#         )
#     else:
#         return render_template(
#             "menu.html",
#             pZroducts=processed_products,
#             cart=cart,
#             cart_len=len(cart),
#             current_page=page,
#             total_pages=total_pages,
#             pagination_links=pagination_links,
#         )
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

    # Get database connection
    conn = get_db('ecommerce.db')
    cursor = conn.cursor()

    # Get total count for pagination
    # This is not required as total pages are already calculated in pagination function
    # cursor.execute('SELECT COUNT(*) FROM products')
    # total = cursor.fetchone()[0]
    # total_pages = (total + per_page - 1) // per_page

    page = int(request.args.get('page', page))
    offset = (page - 1) * per_page

    # Base query
    query = '''
        SELECT product_id, name, price, images, section, category, data
        FROM products
    '''
    params = []

    # Handle filters if present
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

    # Add pagination
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])

    # Execute final query
    cursor.execute(query, params)
    products = cursor.fetchall()
    full_product = products
    print(len(products))
    # Get cart items
    cart_conn = get_db_connection()
    cart_cursor = cart_conn.cursor()
    cart_cursor.execute('SELECT * FROM cart')
    cart_items = cart_cursor.fetchall()
    cart_conn.close()
    cart = [dict(item) for item in cart_items]

    # Process products
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
    print("calling paginator:", page)

    # Generate pagination links
    pagination_links = generate_pagination_links(page, total_pagez.get_total_pages())
    # if request.method == 'GET':
    #     pagination_links = generate_pagination_links(page, total_pagez.get_total_pages())

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

@app.route('/api/products')
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = 9  # Products per page

    # Fetch products from database
    products = Product.query.paginate(page=page, per_page=per_page)

    return jsonify({
        'products': [product.to_dict() for product in products.items],
        'pagination': {
            'current_page': page,
            'total_pages': products.pages,
            'total_items': products.total
        }
    })


# def get_shop_data():
#     page = int(request.args.get('page', 1))
#     per_page = 20
#     offset = (page - 1) * per_page

#     # Get database connection
#     conn = get_db('ecommerce.db')
#     cursor = conn.cursor()

#     # Base query
#     query = '''
#         SELECT product_id, name, price, images, section, category, data
#         FROM products
#     '''
#     params = []

#     # Handle filters if present
#     if filterz.get_current_filters():
#         filters = filterz.get_current_filters()
#         filter_conditions = []
#         for filter_id in filters:
#             clean_filter = filter_id
#             for prefix in ['category-', 'men-', 'women-', 'body-bath-', 'brand-']:
#                 if clean_filter.startswith(prefix):
#                     the_category = clean_filter.replace(prefix, '')
#                     the_section = prefix[:-1]
#                     filter_conditions.append('(LOWER(section) LIKE ? and LOWER(category) LIKE ?)')
#                     params.extend([f'%{the_section.lower()}%', f'%{the_category.lower()}%'])

#         if filter_conditions:
#             query += ' WHERE ' + ' OR '.join(filter_conditions)

#     # Add pagination
#     query += ' LIMIT ? OFFSET ?'
#     params.extend([per_page, offset])

#     # Execute final query
#     cursor.execute(query, params)
#     products = cursor.fetchall()

#     # Get cart items
#     cart_conn = get_db_connection()
#     cart_cursor = cart_conn.cursor()
#     cart_cursor.execute('SELECT * FROM cart')
#     cart_items = cart_cursor.fetchall()
#     cart_conn.close()
#     cart = [dict(item) for item in cart_items]

#     # Process products
#     processed_products = []
#     total_pagez.set_total_pages(int(len(get_all_products())/20))

#     for product in products:
#         product_dict = dict(product)
#         product_dict['images'] = json.loads(product_dict['images'])
#         product_dict['data'] = json.loads(product_dict['data'])
#         processed_products.append(product_dict)

#     conn.close()

#     # Generate pagination links
#     pagination_links = generate_pagination_links(page, total_pagez.get_total_pages())

#     # Prepare response data
#     response_data = {
#         'products': processed_products,
#         'cart': cart,
#         'cart_len': len(cart),
#         'current_page': page,
#         'total_pages': total_pagez.get_total_pages(),
#         'filters': list(set(filterz.get_current_filters())),
#         'pagination_links': pagination_links
#     }

#     return jsonify(response_data)



@app.route("/api/shop_data", methods=['GET',"post"])
def api_shop_data():
    try:
        # Get page number from request, default to 1
        page = int(request.args.get('page', 1))
        per_page = 20  # Products per page
        offset = (page - 1) * per_page
        print(request.args.get('page'))
        if not request.args.get('page'):
            filterz.set_current_filters=[]
        print(filterz.get_current_filters())

        # Get database connection
        conn = get_db('ecommerce.db')
        cursor = conn.cursor()

        # Base query
        query = '''
            SELECT product_id, name, price, images, section, category, data
            FROM products
        '''
        params = []

        # Handle category filtering
        categories_param = filterz.get_current_filters()

        if categories_param:
            try:
                selected_categories = filterz.get_current_filters()
                if selected_categories:
                    category_conditions = []
                    for category in selected_categories:
                        # Remove prefixes like 'category-', 'men-', etc.
                        clean_category = category.split('-')[-1]
                        category_conditions.append(
                            '(LOWER(section) LIKE ? OR LOWER(category) LIKE ?)'
                        )
                        params.extend([f'%{clean_category.lower()}%', f'%{clean_category.lower()}%'])

                    query += ' WHERE ' + ' OR '.join(category_conditions)
            except json.JSONDecodeError:
                pass  # Ignore if categories can't be parsed

        # Handle price filtering
        min_price = request.args.get('minPrice')
        max_price = request.args.get('maxPrice')
        if min_price and max_price:
            if 'WHERE' in query:
                query += ' AND price BETWEEN ? AND ?'
            else:
                query += ' WHERE price BETWEEN ? AND ?'
            params.extend([min_price, max_price])

        # Count total products after filtering
        count_query = f"SELECT COUNT(*) as total FROM ({query}) as filtered_products"
        cursor.execute(count_query, params)
        total_products = cursor.fetchone()['total']

        # Add pagination to query
        query += ' LIMIT ? OFFSET ?'
        params.extend([per_page, offset])

        # Execute final query
        cursor.execute(query, params)
        products = cursor.fetchall()

        # Process products
        processed_products = []
        for product in products:
            product_dict = dict(product)
            # Safely parse JSON fields
            try:
                product_dict['images'] = json.loads(product_dict['images'])
            except json.JSONDecodeError:
                product_dict['images'] = []

            processed_products.append(product_dict)

        # Calculate total pages
        total_pages = (total_products + per_page - 1) // per_page
        print("shoppin data.........")
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


    target_category = None
    related_products=[]
    for product in products:
        print(product['product_id'])
        if int(product['product_id']) == int(id):

            target_category = product['category']
            target_section = product['section']
            for product1 in products:
                if product1['category'] == target_category and product1['section'] == target_section:
                    related_products.append(product1)
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
            def get_cart():
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM cart')
                items = cursor.fetchall()
                conn.close()
                return [dict(item) for item in items]

            if len(results)>1:
                return render_template("pv.html", product=product,data=results[0],colors=results[1]["other-colors"],id=id,cart=cart,cart_len=len(cart),os=os,related_products=related_products[:6],get_cart=get_cart)
            else:
                return render_template("pv.html", product=product,data=results[0],colors=[],id=id,cart=cart,cart_len=len(cart),os=os,related_products=related_products[:6],get_cart=get_cart)

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

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        cart_items = request.form
       
        selected_ids = {int(id) for id, value in cart_items.items() if value == "1"}

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cart')
        items = cursor.fetchall()
        conn.close()

        # Filter cart items based on selected IDs
        cart = [dict(item) for item in items if item["id"] in selected_ids]
        totals= [{item["id"]:float(item["quantity"]*float(item["price"]))} for item in cart]
        sub_total = sum([float(i[a]) for i in totals for a in i])
        print(sub_total)
        return render_template("checkout.html", cart=cart,totals=totals,sub_total=sub_total)
@app.route("/get-cart-items")
def get_cart_itemz():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart')
    items = cursor.fetchall()
    conn.close()
    cart = [dict(item) for item in items]
    return jsonify({"cart":cart})
@app.route("/set_checkout")
def set_checkout():
    total = request.form.get("total")
    items = request.form.get("items")
    return [total,items]
@app.route('/api/products')
def api_products():
    """Fetch products data to be used in the product listing frontend."""
    products = get_all_products()
    for product in products:
        product['images'] = json.loads(product['images'])
        product['data'] = product['data']
    print(products)  # Debugging: Print out product data on the server-side
    return jsonify(products)
@app.errorhandler(401)
def unauthorized(e):
    return render_template('401.html'), 401

if __name__== "__main__":
	app.run(debug=True)
