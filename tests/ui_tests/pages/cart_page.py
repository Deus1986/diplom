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
    def cart_should_have_products(self, quantity):
        browser.element('.GoodsBlock-module__count--WC7jV').should(have.text(f'{quantity} товар'))

    @allure.step("Click delete button in cart")
    def click_delete_button_in_cart(self):
        browser.element('.CheckoutCard-module__deleteButton--JlUTL').click()

    @allure.step("Empty cart should have button 'Начать покупки'")
    def empty_cart_should_have_button(self):
        browser.element('.Button-module__green--bJg1j').should(have.text('Начать покупки'))
