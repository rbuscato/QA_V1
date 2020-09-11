from selenium.webdriver.common.by import By

import pytest

class ConfirmPage:

    #constructor... accept the driver from calling test
    def __init__(self,driver):
        self.driver = driver

    searchResult = (By.XPATH, "//span[contains(text(),'www.cheerios.com')]")

    #  Return the next expected page when user clicks 'shop items' :
    #def shopItems(self):
    #    self.driver.find_element(*HomePage.shop).click()
    #    checkoutPage = CheckoutPage(self.driver)
    #    return checkoutPage

        #optimization :   now above replaces below....
        #return self.driver.find_element(*HomePage.shop)
        # add * to deserialize the tuple -- above.
        #driver.find_element_by_css_selector("a[href*='shop']").click()

    def getSearchResult(self):
        return self.driver.find_element(*ConfirmPage.searchResult)

