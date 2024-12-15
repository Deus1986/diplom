import allure

from data.common_data import st_petersburg_store
from tests.api_tests.api_helper.requests import *


def test_storelocator():
    response_get_info_about_storage = get_info_about_storage(st_petersburg_store.branch_id)
    response_json = response_get_info_about_storage.json()

    with allure.step("Response status code is 200"):
        assert response_get_info_about_storage.status_code == 200

    with allure.step(f"Response should have branch id {st_petersburg_store.branch_id}"):
        assert response_json['payload']['branchId'] == st_petersburg_store.branch_id

    with allure.step(f"Response should have city id {st_petersburg_store.city_id}"):
        assert response_json['payload']['cityId'] == st_petersburg_store.city_id

    with allure.step(f"Response should have region id {st_petersburg_store.region_id}"):
        assert response_json['payload']['regionId'] == st_petersburg_store.region_id

    with allure.step(f"Response should have region name {st_petersburg_store.region_name}"):
        assert response_json['payload']['regionName'] == st_petersburg_store.region_name

    with allure.step(f"Response should have contact phone {st_petersburg_store.contact_phone}"):
        assert response_json['payload']['contactPhone'] == st_petersburg_store.contact_phone
