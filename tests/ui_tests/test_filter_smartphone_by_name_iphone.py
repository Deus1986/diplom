import allure
from allure_commons.types import Severity

from application import *


@allure.tag('UI')
@allure.feature('UI')
@allure.story('Filters')
@allure.title('Filter smartphone by name iphone')
@allure.severity(Severity.CRITICAL)
def test_filter_smartphone_by_name_iphone():
    app.main_page.open_page()
    app.main_page.open_catalog_menu()
    app.main_page.click_smartphone_in_catalog_menu()
    app.smartphone_page.choose_filter("Apple")
    app.smartphone_page.search_results_should_have_text("Apple")
