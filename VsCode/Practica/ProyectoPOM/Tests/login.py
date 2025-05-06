from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from ProyectoPOM.Pages.BasePage import basePage
from ProyectoPOM.Pages.LoginPage import loginPage


class loginTest(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
                cls.driver = basePage.setChromeDriver()
        
        def testLogin(self):
                login = loginPage(self.driver)
                login.navigateToLogin()
                login.setUsername("Admin")
                login.setPassword("admin123")
                login.clickOnButton()
                base = basePage(self.driver)
                base.isValidationTrue(login.isTimeToWorkPresent())
                print(login.getText())
                base.isValidationEqualTo(login.getText(), 'This Week')

        @classmethod
        def tearDownClass(cls):
                cls.driver.quit()


if __name__ == "__main__":
         unittest.main()