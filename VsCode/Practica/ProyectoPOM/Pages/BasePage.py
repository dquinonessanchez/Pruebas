from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

class basePage():

    driver:webdriver

    def __init__(self, driver:webdriver):
        self.driver = driver
        pass

    def visit(self, baseUrl):
        self.driver.get(baseUrl)

    def setChromeDriver()->webdriver:

        cService = webdriver.ChromeService(executable_path='C:/Program Files (x86)/chromedriver.exe')
        driver = webdriver.Chrome(service = cService)
        return driver
    
    def doElementExistXpath(self, locator)->bool:
        self.driver.find_element(By.XPATH, locator)
        return True
    
    def isValidationTrue(self, variable:bool):
        assert variable is True, "El valor no es igual"

    def isValidationEqualTo(self, variable1:str, variable2:str):
        assert variable1 == variable2, "El valor no es igual"