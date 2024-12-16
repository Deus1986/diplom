import allure
import requests
from selene import browser

from config import config


def allure_screenshot():
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='Screenshot',
        attachment_type=allure.attachment_type.PNG
    )


def allure_page_source():
    allure.attach(
        browser.driver.page_source,
        name='Page source XML',
        attachment_type=allure.attachment_type.XML
    )


def add_logs():
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', allure.attachment_type.TEXT, '.log')


def add_video_web():
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, allure.attachment_type.HTML, '.html')


def allure_mobile_video(session_id):
    browser_stack_session = requests.get(
        f'https://api-cloud.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(config.user_name, config.access_key)).json()
    video_url = browser_stack_session['automation_session']['video_url']

    allure.attach(
        "<html><body>"
        "<video width='100%' height='100%' controls autoplay>"
        f"<source src='{video_url}' type='video/mp4'>"
        "</video>"
        "</body></html>",
        name='mobile video',
        attachment_type=allure.attachment_type.HTML
    )
