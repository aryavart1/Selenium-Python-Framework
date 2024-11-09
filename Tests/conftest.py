import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# import time
driver = None

"""Service class sees what version of Chromedriver is installed in the local and runs the Chrome browser accordingly, It
makes runtime faster as Selenium manager doesn't need to identify what version of Chromedriver needs to be installed."""

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):

    global driver
    browser_name = request.config.getoption("browser_name")
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

    # passing driver obj from the class to the request instance and returning the driver obj

    """ passing local driver from fixture to the class driver, if the class uses this fixture in that class if there is
    a driver variable than the local driver will be assigned to it"""

    request.cls.driver = driver  # passing driver from the fixture to the TC

    # return driver (This method will not work as the yeild statement is present)
    yield
    driver.close()



