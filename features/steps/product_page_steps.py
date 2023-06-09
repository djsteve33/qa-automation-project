from selenium.webdriver.common.by import By
from behave import then, when, given
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.XPATH, "//button[@class='product-form__submit button button--secondary button--full-width']")

@when('Click to add product to cart')
def click_add_to_cart(context):
    context.app.product_page.add_product_to_cart()

@given('Open Product {product_name} Details page')
def open_product(context, product_name):
    context.app.main_page.open_product(product_name)

@then('Verify {expected_text} has been added to cart')
def verify_add_to_cart(context, expected_text):
    context.app.product_page.verify_product_added(expected_text)

@when('Click "View Cart"')
def view_my_cart(context):
    context.app.product_page.click_view_cart()


