"""
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""

from PageObjects.CheckOutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        # creating homepage obj to pass driver as an argument
        home_page = HomePage(self.driver)
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

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        confirmpage = check_out_page.checkOutItems()
        log.info("Entering country name as ind")
        self.driver.find_element_by_id("country").send_keys("ind")
        # time.sleep(5)


        self.verifyLinkPresence("India")

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)
