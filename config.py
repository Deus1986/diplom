from typing import Literal

from appium import webdriver
from appium.options.android import UiAutomator2Options
from pydantic_settings import BaseSettings
from selene import browser

from data.resources import resource_path


class Config(BaseSettings):
    remote_url: str = ''
    browser_platform: Literal['android', 'ios'] = 'android'
    platformVersion: str = ''
    browser_name: str = 'chrome'
    timeout: float = 8.0
    browser_version: str = '122'
    user_name: str = ''
    access_key: str = ''
    login_selenoid: str = ''
    password_selenoid: str = ''
    deviceName: str = ''
    appWaitActivity: str = ''
    app: str = ''
    context: Literal['local_web', 'remote_web', 'bstack', 'local_mobile'] = 'remote_web'
    window_height: int = 900
    window_width: int = 1600


if Config().context == 'local_mobile':
    config = Config(_env_file=resource_path('.env.local_emulator'))

if Config().context == 'bstack':
    config = Config(_env_file=(resource_path('.env'), resource_path('.env.bstack')))

if Config().context == 'remote_web':
    config = Config(_env_file=resource_path('.env'))


def run_localy_android():
    options = UiAutomator2Options()
    app = resource_path(config.app)
    options.load_capabilities({
        'appWaitActivity': config.appWaitActivity,
        'app': str(app)
    })
    browser.config.timeout = config.timeout
    browser.config.driver = webdriver.Remote(config.remote_url, options=options)


def run_bstack_android():
    options = UiAutomator2Options()
    options.load_capabilities({
        'appWaitActivity': config.appWaitActivity,
        'app': config.app,
        "deviceName": config.deviceName,
        "platformVersion": config.platformVersion,
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": config.user_name,
            "accessKey": config.access_key
        }
    })
    browser.config.timeout = config.timeout
    browser.config.driver = webdriver.Remote(config.remote_url, options=options)
