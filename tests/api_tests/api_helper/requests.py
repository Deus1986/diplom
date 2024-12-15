import requests

from config import config


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
    response = requests.post(config.api_base_url + 'public-api_helper/checkout/v2/batch/order', json=payload)
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
    response = requests.patch(
        config.api_base_url + f'public-api_helper/checkout/v2/order/{order_id}/basket/1/quantity',
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
    response = requests.delete(config.api_base_url + f'public-api_helper/checkout/v2/order/{order_id}/basket/1/remove',
                               params=params, headers=headers)
    return response


def get_info_about_storage(store_code):
    response = requests.get(f'https://api.shop.megafon.ru/storelocator/get-branch/{store_code}')
    return response


def get_info_about_stores_for_product(eshop_id, region_id, good_id):
    params = {
        "city": 0,
        "eshopId": eshop_id,
        "region": region_id,
        "goodId\[\]": good_id,
        "withCache": 1
    }

    response = requests.get(
        'https://api.shop.megafon.ru/storelocator?city=0&eshopId=27&region=260&goodId\[\]=187953&withCache=1',
        params=params)
    return response
