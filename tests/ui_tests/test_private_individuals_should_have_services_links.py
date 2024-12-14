from application import app


def test_private_individuals_should_have_services_links():
    app.main_page.open_page()
    app.main_page.open_private_individuals_link()
    app.private_individuals_page.page_should_have_services_links()
