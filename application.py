from tests.ui_tests.pages.cart_page import CartPage
from tests.ui_tests.pages.main_page import MainPage
from tests.ui_tests.pages.private_individuals_page import PrivateIndividualsPage
from tests.ui_tests.pages.smartphone_page import SmartphonePage


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.cart_page = CartPage()
        self.smartphone_page = SmartphonePage()
        self.private_individuals_page = PrivateIndividualsPage()


app = Application()
