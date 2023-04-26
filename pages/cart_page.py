from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

   CART_PAGE = (By.XPATH, "//h1[contains(text(), 'Your cart')]")

def verify_cart_page_opens(self, expected_text, *CART_PAGE):
        actual_text = self.driver.find_element(*CART_PAGE).text
        assert expected_text == actual_text, \
            f'Checking by locator {CART_PAGE}. Expected {expected_text}, but got {actual_text}'
