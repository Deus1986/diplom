import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from config import config


@allure.tag('Mobile')
@allure.feature('Mobile')
@allure.story('SIM card')
@allure.title('No access to sim card link')
@allure.severity(Severity.CRITICAL)
def test_no_access_to_sim_card_link():
    if config.browser_platform == "ios":
        pytest.skip("This test for android")

    with allure.step('Verify main page opened'):
        browser.element(
            (AppiumBy.XPATH, '//android.view.View[@text="Добро пожаловать в Личный кабинет МегаФона "]')).should(
            have.text('Добро пожаловать в Личный кабинет МегаФона'))

    with allure.step('Click no access to sim card link'):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Нет доступа к SIM-карте"]')).click()

    with allure.step('No access to sim card link page should have text "Обратитесь в поддержку по номеру:"'):
        browser.element(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="Обратитесь в поддержку по номеру:"]')).should(
            have.text('Обратитесь в поддержку по номеру:'))
