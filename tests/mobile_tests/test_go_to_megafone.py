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
        if config.context == "bstack":
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                             'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                             'FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/'
                                             'android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.'
                                             'WebView/android.view.View/android.view.View/android.view.View/android.'
                                             'view.View/android.view.View/android.view.View[6]')).click()
        else:
            browser.element((AppiumBy.XPATH,
                             '//android.view.View[@resource-id="root"]/android.view.View/android.view.View/'
                             'android.view.View/android.view.View[3]')).click()

    with (step('Choose plastic sim card')):
        if config.context == "bstack":
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                             'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                             'FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/'
                                             'android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.'
                                             'WebView/android.view.View/android.view.View[2]/android.view.View/'
                                             'android.app.Dialog/android.view.View/android.view.View/android.view.'
                                             'View[2]/android.view.View[1]/android.view.View/android.widget.T'
                                             'extView[1]')).should(have.text('SIM-карта'))
        else:
            browser.element((AppiumBy.XPATH, '//android.view.View[@text="SIM-карта"]')
                            ).should(have.text('SIM-карта'))
