from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class ProductPage(Page):

    ADD_TO_CART_BTN = (By.XPATH, "//button[@class='product-form__submit button button--secondary button--full-width']")
    VERIFY_ADDED_TO_CART = (By.XPATH, "//h1[contains(text(), 'SPF30')]")
    #VIEW_CART = (By.XPATH, "//a[contains(text(), 'View cart')]")
    VIEW_CART = (By.XPATH, "//div[@class='button-container']/button")

    def add_product_to_cart(self):
        return self.driver.find_element(*self.ADD_TO_CART_BTN).click()

    def verify_product_added(self, expected_text):
        actual_text = self.driver.find_element(*self.VERIFY_ADDED_TO_CART).text
        assert expected_text == actual_text, \
                f'Expected {expected_text}, but got {actual_text}'

        sleep(2)

    def click_view_cart(self):
        #self.driver.find_element(*self.VIEW_CART).click()
        self.wait_for_element_click(*self.VIEW_CART)
