from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """

    # service = Service(r"C:\Users\swomb\OneDrive\Documents\Careerist\Git Lesson\QA Automation\qa-automation-project\geckodriver.exe")

    ##### FIREFOX ########
    # options = FirefoxOptions()
    # #options.headless = True
    # options.binary_location = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
    # context.driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
    ######################

    # context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox(service=service)

    # # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # service = ChromeService("chromedriver.exe")
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )

    # for browerstack ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'stevewomble_yFi4LI'
    # bs_key = 'KpFewtgw342Jbeq47FRC'
    #
    # desired_cap = {
    #     'browserName': 'Firefox',
    #     'bstack:options': {
    #         'os': 'Windows',
    #         'osVersion': '10'
    #
    #     }
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    #


    # Mobile-Web Emulator
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
