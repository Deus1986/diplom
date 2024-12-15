import os

import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import config


@pytest.fixture()
def set_browser_window_size():
    browser.config.window_height = 1600
    browser.config.window_width = 900


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    if config.web_context == 'local':
        browser.config.base_url = "https://spb.shop.megafon.ru/"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # options.page_load_strategy = "eager"
        options.add_argument('--headless')
        browser.config.timeout = 8
        browser.config.driver_options = options
        # browser.config.driver.maximize_window()

    if config.web_context == 'remote':
        browser.config.base_url = "https://spb.shop.megafon.ru/"
        options = Options()
        capabilities = {
            "browserName": "chrome",
            "browserVersion": 100,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(capabilities)
        options.add_argument("window-size=1920,1080")

        driver = webdriver.Remote(
            command_executor=f"https://{config.login_selenoid}:{config.password_selenoid}"
                             f"@selenoid.autotests.cloud/wd/hub",
            options=options)

        browser.config.driver = driver

    yield
    browser.quit()
