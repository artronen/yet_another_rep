from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_shold_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_login_page(browser):
    link_2 = "http://selenium1py.pythonanywhere.com/es/accounts/login/"
    page = LoginPage(browser, link_2)
    page.should_be_login_form()
    page.should_be_register_form()
