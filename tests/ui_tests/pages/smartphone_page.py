import pytest
from selene import browser, be, command, have


class MainPage:
    def __init__(self):
        pass

    def search_results_should_have_iphone_16(self, value):
        elements = browser.all('.b-good__title-link')
        for i in range(len(elements)):
            elements[i].should(have.text("iPhone 16"))
    # def fill_permanent_address(self, value):
    #     browser.element('//textarea[@id="permanentAddress"]').type(value)
    #
    # def scroll_to_element(self):
    #     browser.element('#permanentAddress').perform(command.js.scroll_into_view)
    #
    # def click_submit(self):
    #     browser.element('#submit').click()
    #
    # def should_have_registered(self, user_data, user_enum):
    #     for i in range(len(user_data)):
    #         browser.element(f"#output > div.border > #{user_enum(i).name}").should(have.text(user_data[f'{i}']))
