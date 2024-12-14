from application import app


def test_main_page_header():
    app.main_page.open_page()
    app.main_page.main_page_header_should_have_links()
    import sys
    import pprint

    pprint.pprint(sys.path)
