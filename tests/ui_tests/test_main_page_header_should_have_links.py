import allure
from allure_commons.types import Severity

from application import app


@allure.tag('UI')
@allure.feature('UI')
@allure.story('Main page')
@allure.title('Main page header')
@allure.severity(Severity.CRITICAL)
def test_main_page_header():
    app.main_page.open_page()
    app.main_page.main_page_header_should_have_links()
    import sys
    import pprint

    pprint.pprint(sys.path)
