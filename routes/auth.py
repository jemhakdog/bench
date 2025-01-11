from flask import render_template

def init_auth_routes(app):
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
        from database import get_all_products
        import json
        products = get_all_products()
        for product in products:
            product['images'] = json.loads(product['images'])
        return render_template("admin-product.html", products=products)

    @app.errorhandler(401)
    def unauthorized(e):
        return render_template('401.html'), 401