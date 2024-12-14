import allure
from selene import browser, be, have
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self):
        self.buy_button = '.b-good__buy'
        self.notification_module = '.Notification-module__wrapper--k8wxI'

    @allure.step("Open browser")
    def open_page(self):
        browser.open("/")
        if browser.element(self.notification_module):
            browser.driver.execute_script(f"$('{self.notification_module}').remove()")

    @allure.step("Fill search field")
    def fill_search_request(self, value):
        browser.element('//input[@data-testid="ChSearch-input"]').should(be.blank).type(value)

    @allure.step("Click search button")
    def click_search_button(self):
        browser.element('//a[@class="ch-search__categories-link"]').click()

    @allure.step("Add product in cart")
    def add_product_in_cart(self):
        ActionChains(browser.driver).scroll_to_element(
            browser.driver.find_element(By.CSS_SELECTOR, self.buy_button)).perform()
        browser.element(self.buy_button).click()
        browser.element('//button[text()="Оформить заказ"]').click()

    @allure.step("Open catalog menu")
    def open_catalog_menu(self):
        browser.element('.gtm-ch-catalog-button').click()

    @allure.step("Click smartphone in catalog menu")
    def click_smartphone_in_catalog_menu(self):
        browser.element('//a[text()="Смартфоны"]').click()

    @allure.step("Open shop contacts")
    def open_shop_contacts(self):
        ActionChains(browser.driver).scroll_to_element(
            browser.driver.find_element(By.CSS_SELECTOR, '.c-footer ')).perform()
        browser.element('//p[text()="Контакты"]').click()

    @allure.step("Contacts should have phone number")
    def contacts_should_have_phone_number(self):
        browser.element('.simplebar-content').should(have.text('Контактный телефон: 8 (800) 550 5858.'))

    @allure.step("Main page header should have links")
    def main_page_header_should_have_links(self):
        header_links_name = {1: "Частным лицам", 2: "Интернет-магазин", 3: "Бизнесу", 4: "Предпринимателям"}
        for i in range(len(header_links_name)):
            browser.all('.ch-service-menu-item-v2__link')[i].should(have.text(header_links_name[i + 1]))

    @allure.step("open_private_individuals_link")
    def open_private_individuals_link(self):
        browser.element('//a[@data-gtm-title="Частным лицам"]').click()
