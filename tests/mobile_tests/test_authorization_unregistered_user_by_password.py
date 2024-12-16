import allure
import pytest
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

from config import config


@allure.tag('Mobile')
@allure.feature('Mobile')
@allure.story('Authorization')
@allure.title('Authorization unregistered user by password')
@allure.severity(Severity.CRITICAL)
def test_authorization_unregistered_user_by_password():
    if config.browser_platform == "ios":
        pytest.skip("This test for android")

    with allure.step('Verify main page opened'):
        browser.element(
            (AppiumBy.XPATH, '//android.view.View[@text="Добро пожаловать в Личный кабинет МегаФона "]')).should(
            have.text('Добро пожаловать в Личный кабинет МегаФона'))

    with allure.step('Click enter by password'):
        if config.context == "bstack":
            browser.element((AppiumBy.XPATH,
                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.'
                             'ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.webkit.'
                             'WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.'
                             'View/android.view.View[2]/android.widget.Button')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Вход по паролю"]')).click()

    with allure.step('Fill phone data'):
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

    with allure.step('Fill password data'):
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

    with allure.step('Click enter button'):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Войти"]')).click()

    with allure.step('Page should have alert'):
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
