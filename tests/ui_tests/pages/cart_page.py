import allure
from selene import browser, have


class CartPage:
    def __init__(self):
        self.notification_module = '.Notification-module__wrapper--k8wxI'

    def open_page(self):
        browser.open("/checkout")
        if browser.element(self.notification_module):
            browser.driver.execute_script(f"$('{self.notification_module}').remove()")

    @allure.step("Add product in cart")
    def cart_should_have_one_product(self):
        browser.element('.GoodsBlock-module__count--WC7jV').should(have.text('1 товар'))
