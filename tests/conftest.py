import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
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
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)


    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(5)


    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
        driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    # passing driver obj from the class to the request instance and returning the driver obj

    """
    passing local driver from fixture to the class driver, if the class uses this fixture in that class if there is
    a driver variable than the local driver will be assigned to it
    """

    request.cls.driver = driver  # passing driver from the fixture to the TC

    # return driver (This method will not work as the yeild statement is present)
    # using yeild statement for tear-down
    yield
    driver.close()



@pytest.fixture(scope="function")
def browser_instance(request):

    global driver
    browser_name = request.config.getoption("browser_name")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(5)


    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
        driver.implicitly_wait(5)

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()

    yield driver  #Before test function execution
    driver.close()  #post your test function execution




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed a screenshot in the HTML report whenever a test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Ensure the reports directory exists
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)

            # Create a screenshot filename and full path
            screenshot_name = report.nodeid.replace("::", "_") + ".png"
            file_path = os.path.join(reports_dir, os.path.basename(screenshot_name))

            # Capture the screenshot
            _capture_screenshot(file_path)

            # Debugging output
            print(f"Screenshot saved at: {file_path}")
            print(f"File exists: {os.path.exists(file_path)}")

            # Use just the filename for embedding in the HTML report
            if os.path.exists(file_path):
                relative_path = os.path.basename(file_path)
                html = f'<div><img src="{relative_path}" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))

            # Debug the HTML being added
            print(f"HTML being added: {html}")

        report.extra = extra

def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)

# Parameterizing the test with multiple data sets using Dictionary