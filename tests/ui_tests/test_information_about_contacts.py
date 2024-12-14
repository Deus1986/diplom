from application import app


def test_information_about_contacts():
    app.main_page.open_page()
    app.main_page.open_shop_contacts()
    app.main_page.contacts_should_have_phone_number()
