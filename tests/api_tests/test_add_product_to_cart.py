import json

import allure
from jsonschema.validators import validate

from data.common_data import tablet_samsung
from data.resources import resource_path
from tests.api_tests.api_helper.requests import add_product_to_cart


@allure.tag('API')
@allure.feature('API')
@allure.story('Add product to cart')
def test_add_product_to_cart():
    response = add_product_to_cart(tablet_samsung.good_id, tablet_samsung.amount)
    response_json = response.json()

    with allure.step("Response status code is 200"):
        assert response.status_code == 200

    with allure.step("Validate response schema"):
        with open(resource_path("data/schemas/add_product_to_cart.json")) as file:
            validate(response.json(), schema=json.loads(file.read()))

    with allure.step(f"Response should have brand name {tablet_samsung.brand}"):
        assert response_json['payload']['order']['basket']['items'][0]['brandName'] == tablet_samsung.brand

    with allure.step(f"Response should have name {tablet_samsung.name}"):
        assert response_json['payload']['order']['basket']['items'][0]['name'] == tablet_samsung.name

    with allure.step(f"Response should have amount {tablet_samsung.amount}"):
        assert response_json['payload']['order']['basket']['items'][0]['amount'] == tablet_samsung.amount

    with allure.step(f"Response should have good id {tablet_samsung.good_id}"):
        assert response_json['payload']['order']['basket']['items'][0]['cart']['goodId'] == tablet_samsung.good_id

    with allure.step(f"Response should have price {tablet_samsung.price}"):
        assert response_json['payload']['order']['basket']['items'][0]['cart']['price'] == tablet_samsung.price

    with allure.step(f"Response should have total price {tablet_samsung.price * tablet_samsung.amount}"):
        assert response_json['payload']['order']['originalTotalPrice'][
                   'priceSum'] == tablet_samsung.price * tablet_samsung.amount
