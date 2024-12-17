import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import config
from data.resources import resource_path
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    base_url = "https://spb.shop.megafon.ru/"
    if config.context == 'local_web':
        browser.config.base_url = base_url
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        browser.config.timeout = config.timeout
        browser.config.driver_options = options
        browser.config.driver.maximize_window()

    if config.context == 'remote_web':
        browser.config.base_url = base_url
        options = Options()
        capabilities = {
            "browserName": config.browser_name,
            "browserVersion": config.browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(capabilities)

        driver = webdriver.Remote(
            command_executor=f"https://{config.login_selenoid}:{config.password_selenoid}"
                             f"@selenoid.autotests.cloud/wd/hub", options=options)

        browser.config.window_width = config.window_width
        browser.config.window_height = config.window_height
        browser.config.driver = driver

    yield
    attach.allure_screenshot()
    attach.allure_page_source()
    attach.allure_add_logs()
    attach.add_video_web()
    browser.quit()
