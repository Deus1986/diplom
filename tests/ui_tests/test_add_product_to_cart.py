import allure
from allure_commons.types import Severity

from application import app


@allure.tag('UI')
@allure.feature('UI')
@allure.story('Cart')
@allure.title('Add product to cart')
@allure.severity(Severity.CRITICAL)
def test_add_product_to_cart(set_browser_window_size):
    app.main_page.open_page()
    app.main_page.add_product_in_cart()
    app.cart_page.cart_should_have_products('1')
