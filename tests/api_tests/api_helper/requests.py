import logging

import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType

api_base_url_spb_shop = 'https://spb.shop.megafon.ru/'
api_base_url_api_shop = 'https://api.shop.megafon.ru/'


def get_url_spb_shop(request_part):
    request = api_base_url_spb_shop + request_part
    return request


def get_url_api_shop(request_part):
    request = api_base_url_api_shop + request_part
    return request


def megafon_shop_api(method, url, **kwargs):
    with step("API Requset"):
        response = requests.request(method, url, **kwargs)
        allure.attach(
            body=response.text,
            name="Response",
            attachment_type=AttachmentType.TEXT,
            extension="txt")
        logging.info(response.status_code)
        logging.info(response.url)
    return response


def add_product_to_cart(good_id, quantity):
    payload = {
        "context": {
            "branchId": 3
        },
        "operations": [
            {
                "operation": "OrderAddGoodToBasket",
                "arguments": {
                    "goodId": good_id,
                    "quantity": quantity
                }
            }
        ]
    }
    url = get_url_spb_shop('public-api/checkout/v2/batch/order')
    response = megafon_shop_api("POST", url, json=payload)
    return response


def change_quantity_of_product(ejwt, order_id, client_id, city_id, quantity):
    payload = {
        "quantity": quantity
    }
    params = {
        "clientId": client_id,
        "cityId": city_id
    }
    headers = {
        "cookie": f"_ejwt = {ejwt}"
    }
    url = get_url_spb_shop(f'public-api/checkout/v2/order/{order_id}/basket/1/quantity')
    response = megafon_shop_api("PATCH", url, json=payload, params=params, headers=headers)
    return response


def delete_order(ejwt, order_id, city_id, client_id):
    params = {
        "clientId": client_id,
        "cityId": city_id
    }
    headers = {
        "cookie": f"_ejwt = {ejwt}"
    }
    url = get_url_spb_shop(f'public-api/checkout/v2/order/{order_id}/basket/1/remove')
    response = megafon_shop_api("DELETE", url, params=params, headers=headers)
    return response


def get_info_about_storage(store_code):
    url = get_url_api_shop(f'storelocator/get-branch/{store_code}')
    response = megafon_shop_api("GET", url)
    return response


def get_info_about_stores_for_product(eshop_id, region_id, good_id):
    params = {
        "city": 0,
        "eshopId": eshop_id,
        "region": region_id,
        "goodId/[]": good_id,
        "withCache": 1
    }
    url = get_url_api_shop('storelocator')
    response = megafon_shop_api("GET", url, params=params)
    return response
