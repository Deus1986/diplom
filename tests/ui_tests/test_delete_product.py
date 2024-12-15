import time

from selene import browser, have
from selene.support.conditions.have import size

from application import app
from data.common_data import tablet_samsung
from tests.api_tests.api_helper.requests import add_product_to_cart


def test_delete_product():
    response_add_product_to_cart = add_product_to_cart(tablet_samsung.good_id, tablet_samsung.amount)
    cookie = response_add_product_to_cart.cookies.get('_ejwt')
    app.cart_page.open_page()
    browser.driver.add_cookie({"name": "_ejwt", "value": cookie, "domain": "spb.shop.megafon.ru"})
    browser.driver.add_cookie({"name": "_ejwt", "value": cookie, "domain": ".megafon.ru"})
    app.cart_page.open_page()
    time.sleep(0.4)
    app.cart_page.cart_should_have_products('5')
    app.cart_page.click_delete_button_in_cart()
    app.cart_page.empty_cart_should_have_button()
