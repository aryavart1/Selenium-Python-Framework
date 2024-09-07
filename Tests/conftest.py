import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    if browser_name == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(options=options, service=service_obj)

    elif browser_name == "firefox":

        service_obj = Service()
        driver = webdriver.Firefox(options=options, service=service_obj)

    elif browser_name == "IE":

        service_obj = Service()
        driver = webdriver.Edge(options=options, service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


