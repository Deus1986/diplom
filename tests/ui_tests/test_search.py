from application import app


def test_search():
    app.main_page.open_page()
    app.main_page.fill_search_request('Iphone 16')
    app.main_page.click_search_button()
    app.smartphone_page.search_results_should_have_text('iPhone 16')
