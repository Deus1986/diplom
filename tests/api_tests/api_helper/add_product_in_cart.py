import requests

from config import config


def add_product_to_cart(ejwt):
    payload = {
        "context": {
            "branchId": 14,
            "orderId": 33964945,
            "clientId": 8534993
        },
        "operations": [
            {
                "operation": "OrderAddGoodToBasket",
                "arguments": {
                    "goodId": 185239,
                    "quantity": 1
                }
            }
        ]
    }
    headers = {
        "cookie": ejwt
    }
    response = requests.post(config.api_base_url + 'public-api/checkout/v2/batch/order', json=payload, headers=headers)
    return response
