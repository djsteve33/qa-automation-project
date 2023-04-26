from pages.base_page import Page


class MainPage(Page):

    def open_product(context, product_name):
        context.driver.get(
            f'https://shop.cureskin.com/collections/for-dry-skin/products/{product_name}/')

