import allure
from selene import browser, have
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class SmartphonePage:
    def __init__(self):
        pass

    @allure.step('Search results should have iphone 16')
    def search_results_should_have_text(self, value):
        elements = browser.all('.b-good__title-link')
        for i in range(len(elements)):
            elements[i].should(have.text(value))

    @allure.step('Choose filter')
    def choose_filter(self, filter_name):
        ActionChains(browser.driver).scroll_to_element(
            browser.driver.find_element(By.XPATH, f'//span[text()="{filter_name}"]')).perform()
        browser.element(f'//span[text()="{filter_name}"]').click()
        browser.element('//span[text()="Применить"]').click()
