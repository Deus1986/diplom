import logging

import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType

from config import config


def megafon_shop_api(method, url, **kwargs):
    with step("API Requset"):
        response = requests.request(method, url, **kwargs)
        allure.attach(
            body=response.text,
            name="Response",
            attachment_type=AttachmentType.TEXT,
            extension="txt")
        logging.info(response.status_code)
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
    response = megafon_shop_api("POST", config.api_base_url_spb_shop + 'public-api/checkout/v2/batch/order',
                                json=payload)
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
    response = megafon_shop_api("PATCH",
                                config.api_base_url_spb_shop + f'public-api/checkout/v2/order/{order_id}'
                                                               f'/basket/1/quantity',
                                json=payload, params=params, headers=headers)
    return response


def delete_order(ejwt, order_id, city_id, client_id):
    params = {
        "clientId": client_id,
        "cityId": city_id
    }
    headers = {
        "cookie": f"_ejwt = {ejwt}"
    }
    response = megafon_shop_api("DELETE",
                                config.api_base_url_spb_shop + f'public-api/checkout/v2/order/{order_id}'
                                                               f'/basket/1/remove',
                                params=params, headers=headers)
    return response


def get_info_about_storage(store_code):
    response = megafon_shop_api("GET", config.api_base_url_api_shop + f'storelocator/get-branch/{store_code}')
    return response


def get_info_about_stores_for_product(eshop_id, region_id, good_id):
    params = {
        "city": 0,
        "eshopId": eshop_id,
        "region": region_id,
        "goodId/[]": good_id,
        "withCache": 1
    }

    response = megafon_shop_api("GET", config.api_base_url_api_shop + 'storelocator', params=params)
    return response
