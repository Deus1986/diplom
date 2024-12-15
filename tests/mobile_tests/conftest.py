import allure_commons
import pytest
from selene import support

from config import *
from utils.attach import *


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    if config.context == 'local':
        run_localy_android()

    if config.context == 'bstack':
        run_bstack_android()

    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield

    allure_screenshot()
    allure_page_source()

    session_id = browser.driver.session_id

    browser.quit()

    if config.context == 'bstack':
        allure_video(session_id)
