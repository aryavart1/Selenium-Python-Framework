import pytest

# from TestData.HomePageData import HomePageData
from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["first_name"])
        homepage.getName().send_keys(getData["first_name"])
        homepage.getEmail().send_keys(getData["last_name"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)

        # Refreshes the page to test new test values
        self.driver.refresh()

    @pytest.fixture(params=[{"first_name": "ark", "last_name": "genesis", "gender": "Male"},
                            {"first_name": "ark1", "last_name": "genesis_1", "gender": "Female"}])
    def getData(self, request):
        return request.param


# Implementing data driven mechanisms

""" 
    # Passing the values as list and treating each tuple as a value
    @pytest.fixture(params=[('test_first_name', 'test_last_name', 'test_gender'), ('test_first_name_2', 'test_last_name_2', 'test_gender_2')])
    def getData(self, request):
        return request.param
        
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param


    #  Parameterizing the test with multiple data sets using Dictionary
    @pytest.fixture(params=[{"test_first_name": "ark", "test_last_name": "genesis", "test_gender": "genx"},
                            {"test_first_name_1": "ark1", "test_last_name_1": "genesis_1", "test_gender_1": "geny"}])
    def getData(self, request):
        return request.param
"""
