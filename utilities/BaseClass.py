import pytest
import logging
import inspect

# setup base class for all utilities
#  let all test_checkGooglePage.py , etc  inherit this class.
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

#from selenium.webdriver.support import Select

import time
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        # capture name of test for the logs.
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # returns filehandler object
        fileHandler = logging.FileHandler("myFrameworkLogfile.log")

        # postpend 's' to treat as string
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        # now we can write to final logger object
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger

    def verifyLinkPresence(self, textToVerify):
        element = WebDriverWait(self.driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT, textToVerify)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)