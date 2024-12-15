from application import app


def test_add_product_to_cart():
    app.main_page.open_page()
    app.main_page.add_product_in_cart()
    app.cart_page.cart_should_have_products('1')
