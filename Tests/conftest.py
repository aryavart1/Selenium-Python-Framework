import pytest

from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")  # the fixture will run once before and after Class
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    service_obj = Service()
    driver = webdriver.Chrome(options=options, service=service_obj)


