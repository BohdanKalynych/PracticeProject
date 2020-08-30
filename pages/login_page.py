from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.endswith("login/")

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), \
                                                            "Login form is not present"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), \
                                                            "Register form is not present"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FORM), \
                                                            "Registration email form is not present"
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_FORM), \
                                                                "Registration password form is not present"
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASS_FORM), \
                                                            "Confirm password form is not present"
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), \
                                                            "Register button is not present"
        email_field[0].send_keys(email)
        password_field[0].send_keys(password)
        confirm_password_field[0].send_keys(password)
        register_btn[0].click()


