"""
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDrX`iverWait
from selenium.webdriver.support import expected_conditions as EC
"""
import time
import unittest
from selenium.webdriver.common.by import By

from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
# from selenium.webdriver.common.action_chains import ActionChains

class TestOne(BaseClass, unittest.TestCase):
    def test_e2e(self):
        log = self.getLogger()

        # creating homepage obj to pass driver as an argument
        home_page = HomePage(self.driver)
        print(self.driver.title)
        log.info(self.driver.title)
        check_out_page = home_page.shopItems()
        log.info("getting all the card titles")
        cards = check_out_page.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                check_out_page.getCardFooter()[i].click()

        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()


        confirm_page = check_out_page.checkOutItems()

        log.info("Entering country name as ind")

        self.driver.find_element(By.ID, "country").send_keys("ind")
        # time.sleep(5)

        self.verifyLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        text_match = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info(f"Text received from application is {text_match}")

        assert "Success! Thank you!" in text_match



if __name__ == "__main__":
    unittest.main()