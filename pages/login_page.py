from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert (
            "login" in browser.current_url
        ), 'Current URL didn\'t contain "login" part'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(
            *LoginPageLocators.LOGIN_FORM
        ), "Login for hasn't present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form hasn't present"
