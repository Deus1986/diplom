import allure

from data.common_data import tablet_samsung, st_petersburg_store
from tests.api_tests.api_helper.requests import add_product_to_cart, delete_order


def test_delete_order():
    response_add_product_to_cart = add_product_to_cart(tablet_samsung.good_id, tablet_samsung.amount)
    cookie = response_add_product_to_cart.cookies.get('_ejwt')
    order_id = response_add_product_to_cart.json()['payload']['order']['orderId']
    client_id = response_add_product_to_cart.json()['payload']['order']['clientId']

    response = delete_order(cookie, order_id, st_petersburg_store.city_id, client_id)
    response_json = response.json()

    with allure.step("Response status code is 200"):
        assert response.status_code == 200

    with allure.step("Response should't have items"):
        assert response_json['payload']['order']['basket']['items'] == []

    with allure.step(f"Response should have order id {order_id}"):
        assert response_json['payload']['order']['orderId'] == order_id

    with allure.step(f"Response should have client id {client_id}"):
        assert response_json['payload']['order']['clientId'] == client_id

    with allure.step(f"Response should have total sum 0"):
        assert response_json['payload']['order']['originalTotalPrice']['priceSum'] == 0

