import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from config import config


def test_no_access_to_sim_card_link():
    if config.browser_platform == "ios":
        pytest.skip("This test for android")

    with step('Verify main page opened'):
        browser.element(
            (AppiumBy.XPATH, '//android.view.View[@text="Добро пожаловать в Личный кабинет МегаФона "]')).should(
            have.text('Добро пожаловать в Личный кабинет МегаФона'))

    with step('Click no access to sim card link'):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Нет доступа к SIM-карте"]')).click()

    with step('No access to sim card link page should have text "Обратитесь в поддержку по номеру:"'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Обратитесь в поддержку по номеру:"]')).should(have.text('Обратитесь в поддержку по номеру:'))

