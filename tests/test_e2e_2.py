# pytest -m smoke   // Tagging
# pytest -n 10 //pytest-xdist plugin you need to run in parallel
# pytest -n 2 -m smoke --browser_name firefox --html=reports/report.html
# from selenium import webdriver

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# chrome driver
from selenium.webdriver.chrome.service import Service
# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# import unittest
import os
import sys

import json
import pytest
from PageObjects.login import LoginPage

test_data_path = '../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)  # load method will covert Json file into Python object
    test_list = test_data["data"]  # for accessing the data inside the mentioned key


@pytest.mark.smoke  # pytest -m smoke
@pytest.mark.parametrize("test_list_item", test_list)  # fixture picks single item from the list
def test_e2e(test_list_item, browser_instance):  # passing fixture data and driver to the function
    driver = browser_instance
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())  # Using method mentioned in Browser
    shop_page = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.getTitle())

    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()
    print("Order is received")

