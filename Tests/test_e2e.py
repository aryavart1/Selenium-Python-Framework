""" Standards of writing Selenium tests in Framework and implementing POM """



from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Tests.utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage


# @pytest.mark.usefixtures("setup")



class TestOne(BaseClass):

    def test_e2e(self):

        homepage = HomePage(self.driver)

        homepage.shopItems().click()


        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        # Chaining of web elements
        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        # Cart button
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        # Checkout button
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        self.driver.find_element(By.ID, "country").send_keys("Ind")

        # Adding Explicit wait
        wait = WebDriverWait(self.driver, 10)
        """presenceOfElementLocated - element is present on the DOM of a page. 
           visibilityOfElementLocated -> element is present on the DOM of a page and visible"""
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in success_text


