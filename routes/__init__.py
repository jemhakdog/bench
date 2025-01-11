"""
Routes package for the e-commerce application.

This package contains all the route modules for different functionalities:
- auth.py: Authentication routes (login, register, etc.)
- cart.py: Shopping cart management routes
- checkout.py: Checkout process routes
- products.py: Product management routes
- shop.py: Shop display and filtering routes
"""

from .auth import init_auth_routes
from .cart import init_cart_routes
from .checkout import init_checkout_routes
from .products import init_product_routes
from .shop import init_shop_routes

__all__ = [
    'init_auth_routes',
    'init_cart_routes',
    'init_checkout_routes',
    'init_product_routes',
    'init_shop_routes'
]