from selenium.webdriver.common.by import By
from behave import then, when
#from time import sleep
from selenium.webdriver.support import expected_conditions as EC

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")

@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    #sleep(2)
    context.driver.wait.until(EC.element_to_be_selected(PRODUCT_PRICE))

@then('Verify {category} department is selected')
def verify_selected_dept(context, category):
    context.app.search_results_page.verify_selected_dept(category)