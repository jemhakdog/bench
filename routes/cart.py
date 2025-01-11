from flask import jsonify, request
from datetime import datetime
from database import get_db_connection

def init_cart_routes(app):
    @app.route('/cart/delete/<id>', methods=['GET', 'DELETE'])
    def delete_cart_product(id):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM cart WHERE id=?", (id,))
        product = cursor.fetchone()

        if not product:
            conn.close()
            return jsonify({'success': False, 'message': 'Product not found in cart'}), 404

        cursor.execute("DELETE FROM cart WHERE id=?", (id,))
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Product successfully removed from cart'}), 200

    @app.route('/cart/add', methods=['POST'])
    def add_cart_item():
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO cart (user_id, product_id, order_date, color, size, quantity, sku, image, name, price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (data['user_id'], data['product_id'], datetime.now(), data['color'], data['size'], 
              data['quantity'], data['sku'], data['image'], data['name'], data['price']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Item added to cart!'}), 201

    @app.route('/cart', methods=['GET'])
    def get_cart_items():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cart')
        items = cursor.fetchall()
        conn.close()
        return jsonify([dict(item) for item in items])

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
        ''', (data['user_id'], data['product_id'], data['color'], data['size'], 
              data['quantity'], data['sku'], data['image'], item_id))
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

    @app.route('/api/cart/count', methods=['GET'])
    def cart_count():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) AS cart_len FROM cart')
        cart_count = cursor.fetchone()['cart_len']
        conn.close()
        return jsonify({'cart_len': cart_count})