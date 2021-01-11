"""
`params['project_url']` will be returned after deploying the application in docker container. So this will be
available in the params parameter in every function and class methods. For E2E testing, Chrome browser driver path is
available in `params['driver_path']`. See below, are examples to write test cases.

1. Method based
def test_add_to_cart(params):
    project_url = params['project_url']
    driver_path = params['driver_path']
    # ...
    # Your code goes here
    # ...


2. Class based
class Test:
    def test_add_to_cart(self, params):
        project_url = params['project_url']
        driver_path = params['driver_path']
        # ...
        # Your code goes here
        # ...


todo: Only headless option
todo: Create webapp class for browser driver
todo: need to check this on server
"""
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HEADLESS = False


def test_cheque_created(params):
    """
    Test cheque created
    """
    project_url = params['project_url']
    driver_path = params['driver_path']
    options = Options()
    options.headless = HEADLESS
    driver = webdriver.Chrome(driver_path, options=options)
    driver.get(project_url)
    driver.find_element_by_name('amount').send_keys('200')
    driver.find_element_by_name('submit').click()
    page_html = driver.page_source
    driver.close()
    assert "ICICI BANK, Chandigarh Branch, 140308" in page_html


def test_cheque_created_with_fraction_amount(params):
    """
    Test cheque created
    """
    project_url = params['project_url']
    driver_path = params['driver_path']
    options = Options()
    options.headless = HEADLESS
    driver = webdriver.Chrome(driver_path, options=options)
    driver.get(project_url)
    driver.find_element_by_name('amount').send_keys('126.23')
    driver.find_element_by_name('submit').click()
    page_html = driver.page_source
    driver.close()
    assert "One Hundred And Twenty Six Point Two Three" in page_html
