import allure
from allure_commons.types import Severity

from application import app


@allure.tag('UI')
@allure.feature('UI')
@allure.story('Private individuals')
@allure.title('Private individuals services links')
@allure.severity(Severity.CRITICAL)
def test_private_individuals_should_have_services_links():
    app.main_page.open_page()
    app.main_page.open_private_individuals_link()
    app.private_individuals_page.page_should_have_services_links()
