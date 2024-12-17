import allure
from allure_commons.types import Severity

from application import app


@allure.tag('UI')
@allure.feature('UI')
@allure.story('Search')
@allure.title('Search by name iphone')
@allure.severity(Severity.CRITICAL)
def test_search():
    app.main_page.open_page()
    app.main_page.fill_search_request('Iphone 16')
    app.main_page.click_search_button()
    app.smartphone_page.search_results_should_have_text('iPhone 16')
