from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings

import tests


class Config(BaseSettings):
    api_base_url: str = 'https://spb.shop.megafon.ru/'
    remote_url: str = ''
    browser_platform: Literal['android', 'ios'] = 'android'
    platformVersion: str = ''
    timeout: float = 4.0
    user_name: str = ''
    access_key: str = ''
    deviceName: str = ''
    appWaitActivity: str = ''
    app: str = ''
    context: str = 'local'


if Config().context == 'local':
    config = Config(_env_file=Path(tests.__file__).parent.parent.joinpath('.env.local_emulator').absolute())
#
# if Config().context == 'bstack':
#     config = Config(_env_file=(Path(tests.__file__).parent.parent.joinpath('.env').absolute(),
#                                Path(tests.__file__).parent.parent.joinpath('.env.bstack').absolute()))
#
#
# def run_localy_android():
#     options = UiAutomator2Options()
#     app = str(Path(tests.__file__).parent.parent.joinpath(config.app).absolute())
#     options.load_capabilities({
#         'appWaitActivity': config.appWaitActivity,
#         'app': app
#     })
#     browser.config.timeout = config.timeout
#     browser.config.driver = webdriver.Remote(config.remote_url, options=options)
#
#
# def run_bstack_android():
#     options = UiAutomator2Options()
#     options.load_capabilities({
#         'appWaitActivity': config.appWaitActivity,
#         'app': config.app,
#         "deviceName": config.deviceName,
#         "platformVersion": config.platformVersion,
#         'bstack:options': {
#             "projectName": "First Python project",
#             "buildName": "browserstack-build-1",
#             "sessionName": "BStack first_test",
#
#             # Set your access credentials
#             "userName": config.user_name,
#             "accessKey": config.access_key
#         }
#     })
#
#     browser.config.timeout = config.timeout
#     browser.config.driver = webdriver.Remote(config.remote_url, options=options)
