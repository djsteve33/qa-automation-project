from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):

    SIGN_IN_HEADER = (By.XPATH, "//*[contains(text(), 'Sign in')]")
    EMAIL_FIELD = (By.XPATH, "//input[@type='email']")
    def verify_sign_in_header(self, expected_result):
        actual_result = self.find_element(*self.SIGN_IN_HEADER).text
        assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

    def verify_email_field(self):
        self.find_element(*self.EMAIL_FIELD)
        # assert expected_result_2 == actual_result_2, f'Expected {expected_result_2} but got actual {actual_result_2}'
