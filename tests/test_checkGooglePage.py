
#
# to run this test from command line :
# /Users/richardbuscato/PycharmProjects/PythonSelfFramework/tests
#   py.test    (test_checkGooglePage.py) is the only test.


from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from pageObjects.HomePage import HomePage
from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass
# we moved to BaseClass --->  @pytest.mark.usefixtures("setup")
# now inherit BaseClass

class TestOne(BaseClass):
    def test_checkGooglePage(self):
        log = self.getLogger()
        log.info("1. get the search field on google home page.")
        # step 01 :
        homePage = HomePage(self.driver)
        homePage.getSearchField().send_keys("cheerios")
        homePage.getButtonGoogleSearch().click()

        time.sleep(3)
        log.info("2. confirm the results page. Find 'www.cheerios.com'. ")
        confirmPage = ConfirmPage(self.driver)
        confirmPage.getSearchResult()

        # Create a utility in BaseClass to handle this.
        # error...WebDriverWait.until(EC.presence_of_element_located(By.LINK_TEXT, "India"))
        #wait = WebDriverWait(self.dr)
        #BaseClass.verifyLinkPresence(self.driver, "India")
        #self.verifyLinkPresence("India")
        #time.sleep(10)

        #checkoutpage.getLinkIndia().click()
        #checkoutpage.getTermsCheckbox().click()