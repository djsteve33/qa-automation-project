from selenium.webdriver.common.by import By
from behave import then

CART_PAGE = (By.XPATH, "//h1[contains(text(), 'Your cart')]")

@then('Verify user is taken to the cart page')
def verify_cart_page(context):
    context.app.cart_page.verify_cart_page_opens(*CART_PAGE)