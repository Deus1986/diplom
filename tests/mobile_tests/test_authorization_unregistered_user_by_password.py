import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from config import config


def test_authorization_unregistered_user_by_password():
    if config.browser_platform == "ios":
        pytest.skip("This test for android")

    with step('Verify main page opened'):
        browser.element(
            (AppiumBy.XPATH, '//android.view.View[@text="Добро пожаловать в Личный кабинет МегаФона "]')).should(
            have.text('Добро пожаловать в Личный кабинет МегаФона'))

    with step('Click enter by password'):
        if config.context == "bstack":
            browser.element((AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.'
                             'ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.webkit.'
                             'WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.'
                             'View/android.view.View[2]/android.widget.Button')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Вход по паролю"]')).click()

    with ((step('Fill phone data'))):
        if config.context == "bstack":
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                             'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                             'FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/'
                                             'android.widget.FrameLayout[2]/android.webkit.WebView/android.'
                                             'webkit.WebView/android.view.View/android.view.View/android.view.View'
                                             '/android.view.View/android.view.View/android.view.View[3]/'
                                             'android.view.View[1]/android.view.View/android.widget.EditText')
                            ).type('9101662381')
        else:
            browser.element(
                (AppiumBy.XPATH, '//android.view.View[@resource-id="root"]/android.view.View/android.view.View'
                                 '/android.view.View/android.view.View[1]/android.view.View/android.view.'
                                 'View[3]/android.view.View[1]/android.view.View/android.widget.EditText')
            ).type('9101662381')

    with (step('Fill password data')):
        if config.context == "bstack":
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                             'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                             'FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/'
                                             'android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.'
                                             'WebView/android.view.View/android.view.View/android.view.View/android.'
                                             'view.View/android.view.View/android.view.View[3]/android.view.View[2]/'
                                             'android.view.View/android.widget.EditText')).click()
            browser.element((AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.'
                             'ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.webkit.'
                             'WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/'
                             'android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/'
                             'android.widget.EditText')).type('abcdefg123')
        else:
            browser.element(
                (AppiumBy.XPATH, '//android.view.View[@resource-id="root"]/android.view.View/android.view.View/'
                                 'android.view.View/android.view.View[1]/android.view.View/android.view.View[3]'
                                 '/android.view.View[2]/android.view.View/android.widget.EditText')
            ).type('abcdefg123')

    with step('Click enter button'):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Войти"]')).click()

    with step('Page should have alert'):
        if config.context == "bstack":
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                             'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                                             'FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/'
                                             'android.widget.FrameLayout[2]/android.webkit.WebView/android.webkit.'
                                             'WebView/android.view.View/android.view.View/android.view.View/android.'
                                             'view.View/android.view.View/android.view.View[1]/android.view.View/'
                                             'android.view.View/android.widget.TextView')
                            ).should(have.text('Этот номер не обслуживается в МегаФоне (Код ошибки: a229)'))
        else:
            browser.element((AppiumBy.XPATH, '//android.view.View[@text="Этот номер не '
                                             'обслуживается в МегаФоне (Код ошибки: a229)"]')
                            ).should(have.text('Этот номер не обслуживается в МегаФоне (Код ошибки: a229)'))
