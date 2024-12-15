import allure

from data.common_data import tablet_samsung, st_petersburg_store
from tests.api_tests.api_helper.requests import get_info_about_stores_for_product


def test_get_info_about_stores_for_product():
    response = get_info_about_stores_for_product(st_petersburg_store.eshop_id, st_petersburg_store.region_id,
                                                 tablet_samsung.good_id)
    response_json = response.json()

    with allure.step("Response status code is 200"):
        assert response.status_code == 200

    with allure.step(
            f"Response office should have city id {st_petersburg_store.city_id} and {st_petersburg_store.region_name}"):
        for i in range(101):
            assert response_json['payload']['offices'][i]['cityId'] == st_petersburg_store.city_id
            assert response_json['payload']['offices'][i]['place'] == st_petersburg_store.region_name
