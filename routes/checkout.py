from flask import request, render_template, jsonify, redirect, url_for
from flask_mail import Mail, Message
from database import get_db_connection

def init_checkout_routes(app):
    # Configure Flask-Mail
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'joblits.co@gmail.com'  # Replace with your email
    app.config['MAIL_PASSWORD'] = 'xvuh racq cbue fskh'     # Replace with your app password
    mail = Mail(app)
    @app.route("/checkout", methods=["GET", "POST"])
    def checkout():
        if request.method == "POST":
            cart_items = request.form
            selected_ids = []
            for i in cart_items:
                try:
                    selected_ids.append(int(i))
                    selected_ids.append(str(i))
                except:
                    pass

            if cart_items is None:
                return jsonify({"error": "No cart data provided"}), 400

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cart')
            items = cursor.fetchall()
            conn.close()

            # Filter cart items based on selected IDs
            cart = [dict(item) for item in items if item["id"] in selected_ids]
            totals = [{item["id"]: float(item["quantity"]*float(item["price"]))} for item in cart]
            sub_total = sum([float(i[a]) for i in totals for a in i])
            # Format sub_total to ensure it's a valid float string
            formatted_total = "{:.2f}".format(sub_total)
            return render_template("checkout.html", cart=cart, totals=totals, sub_total=formatted_total)

    @app.route("/bill", methods=['GET', 'POST'])
    def bill():
        if request.method == 'POST':
            email = request.form.get('email')
            cash_paid = float(request.form.get('cash'))
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cart')
            items = cursor.fetchall()
            conn.close()
            
            # Calculate total
            total = sum(item['price'] * item['quantity'] for item in items)
            
            # Send email receipt
            msg = Message('Your Purchase Receipt',
                        sender=app.config['MAIL_USERNAME'],
                        recipients=[email])
            
            msg.html = render_template('email_receipt.html',
                                     items=items,
                                     total=total,
                                     cash_paid=cash_paid)
            
            mail.send(msg)
            
            # After sending email, redirect to shop instead of showing bill
            return redirect(url_for('shop'))
        
        return redirect(url_for('shop'))

    @app.route("/set_checkout")
    def set_checkout():
        total = request.form.get("total")
        items = request.form.get("items")
        return [total, items]
