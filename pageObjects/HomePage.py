from selenium.webdriver.common.by import By

import pytest

class HomePage:

    #constructor... accept the driver from calling test
    def __init__(self,driver):
        self.driver = driver

    search = (By.XPATH, "//input[@name='q']")
    buttonGoogleSearch = (By.CSS_SELECTOR, "[name='btnK']")
    #name = (By.CSS_SELECTOR, "")
    #email = (By.NAME, "email")
    #gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    #submit = (By.CSS_SELECTOR, "input[value='Submit']")

    #  Return the next expected page when user clicks 'shop items' :
    #def shopItems(self):
    #    self.driver.find_element(*HomePage.shop).click()
    #    checkoutPage = CheckoutPage(self.driver)
    #    return checkoutPage

        #optimization :   now above replaces below....
        #return self.driver.find_element(*HomePage.shop)
        # add * to deserialize the tuple -- above.
        #driver.find_element_by_css_selector("a[href*='shop']").click()

    def getSearchField(self):
        return self.driver.find_element(*HomePage.search)

    def getButtonGoogleSearch(self):
        return self.driver.find_element(*HomePage.buttonGoogleSearch)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
