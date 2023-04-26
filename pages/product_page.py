from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):

    ADD_TO_CART_BTN = (By.XPATH, "//button[@class='product-form__submit button button--secondary button--full-width']")
    VERIFY_ADDED_TO_CART = (By.XPATH, "//a[contains(text(), 'SPF30')]")
    VIEW_CART = (By.XPATH, "//a[contains(text(), 'View cart')]")
def add_product_to_cart(self, *ADD_TO_CART_BTN):
    return self.driver.find_element(*ADD_TO_CART_BTN).click()

def verify_product_added(self, expected_text, *VERIFY_ADDED_TO_CART):
    actual_text = self.driver.find_element(*VERIFY_ADDED_TO_CART).text
    assert expected_text == actual_text, \
            f'Checking by locator {VERIFY_ADDED_TO_CART}. Expected {expected_text}, but got {actual_text}'

def click_view_cart(self, *VIEW_CART):
        self.driver.find_element(*VIEW_CART).click()
