import allure
from selene import browser, have
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from data.common_data import Services


class PrivateIndividualsPage:
    def __init__(self):
        pass

    @allure.step("Add product in cart")
    def cart_should_have_one_product(self):
        browser.element('.GoodsBlock-module__count--WC7jV').should(have.text('1 товар'))

    @allure.step("Page should have services links")
    def page_should_have_services_links(self):
        ActionChains(browser.driver).scroll_to_element(
            browser.driver.find_element(By.CSS_SELECTOR, '.main-page-services__tab-item')).perform()
        elements = browser.all('.main-page-services__tab-item')
        for i in range(len(elements)):
            elements[i].should(have.text(Services.services_names()[i]))
