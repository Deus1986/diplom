import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from config import config


def test_go_to_megafone():
    if config.browser_platform == "ios":
        pytest.skip("This test for android")

    with step('Verify main page opened'):
        browser.element(
            (AppiumBy.XPATH, '//android.view.View[@text="Добро пожаловать в Личный кабинет МегаФона "]')).should(
            have.text('Добро пожаловать в Личный кабинет МегаФона'))

    with step('Click go to megafone'):
        browser.element((AppiumBy.XPATH,
                         '//android.view.View[@resource-id="root"]/android.view.View/android.view.View/'
                         'android.view.View/android.view.View[3]')).click()

    with step('Choose plastic sim card'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="SIM-карта Пластиковая"]')).click()

    with step('Page should have text choose how to activate the tariff'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@text="Выберите, как подключить тариф"]')).should(
            have.text('Выберите, как подключить тариф'))
