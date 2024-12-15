import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from config import config


def test_link_nearest_offices():
    if config.browser_platform == "ios":
        pytest.skip("This test for android")

    with step('Verify main page opened'):
        browser.element(
            (AppiumBy.XPATH, '//android.view.View[@text="Добро пожаловать в Личный кабинет МегаФона "]')).should(
            have.text('Добро пожаловать в Личный кабинет МегаФона'))

    with step('Click nearest_offices'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc="Ближайшие салоны"]')).click()

    with step('Nearest offices page should have buttons salons and coverage'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@text="Салоны"]')).should(have.text('Салоны'))
        browser.element((AppiumBy.XPATH, '//android.view.View[@text="Покрытие"]')).should(have.text('Покрытие'))
