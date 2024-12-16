import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import config
from utils import attach


@pytest.fixture()
def set_browser_window_size():
    browser.config.window_height = config.window_height
    browser.config.window_width = config.window_width


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    if config.web_context == 'local':
        browser.config.base_url = "https://spb.shop.megafon.ru/"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        browser.config.timeout = config.timeout
        browser.config.driver_options = options
        browser.config.driver.maximize_window()

    if config.web_context == 'remote':
        browser.config.base_url = "https://spb.shop.megafon.ru/"
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
        options.add_argument("window-size=1920,1080")

        driver = webdriver.Remote(
            command_executor=f"https://{config.login_selenoid}:{config.password_selenoid}"
                             f"@selenoid.autotests.cloud/wd/hub", options=options)

        browser.config.driver = driver

    yield
    attach.allure_screenshot()
    attach.allure_page_source()
    attach.add_logs()
    attach.add_video_web()
    browser.quit()
