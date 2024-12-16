import allure
from allure_commons.types import Severity

from application import app


@allure.tag('UI')
@allure.feature('UI')
@allure.story('Company info')
@allure.title('Information about contacts')
@allure.severity(Severity.CRITICAL)
def test_information_about_contacts():
    app.main_page.open_page()
    app.main_page.open_shop_contacts()
    app.main_page.contacts_should_have_phone_number()
