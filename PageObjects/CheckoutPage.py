class HomePage:

    # creating constructor to pass the driver
    def __init__(self, driver):
        self.driver = driver

    products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")