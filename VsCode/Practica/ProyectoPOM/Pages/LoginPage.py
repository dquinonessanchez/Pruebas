from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from ProyectoPOM.Pages.BasePage import basePage
from selenium.common.exceptions import NoSuchElementException



class loginPage():

    baseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    usernameTextBox = "//input[@name='username']"
    passwordTextBox = "//input[@name='password']"
    loginButton = "//button[@type='submit']"
    timeToWorkText = "//p[@class='oxd-text oxd-text--p'][text()[contains(.,'Time at Work')]]"
    timeThisWeekText = "//p[@class='oxd-text oxd-text--p'][text()[contains(., 'This Week')]]"

  
    def __init__(self, driver:webdriver):
        self.driver=driver
        self.base = basePage(driver)


    def navigateToLogin(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print(f'Estamos en: {self.driver.title}')
        self.driver.implicitly_wait(10)


    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.usernameTextBox).clear()
        self.driver.find_element(By.XPATH, self.usernameTextBox).send_keys(username)
        self.driver.implicitly_wait(3)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.passwordTextBox).clear()
        self.driver.find_element(By.XPATH, self.passwordTextBox).send_keys(password)
        self.driver.implicitly_wait(3)

    def clickOnButton(self):
        self.driver.find_element(By.XPATH, self.loginButton).click()
        self.driver.implicitly_wait(10)

    def isTimeToWorkPresent(self)->bool:
     
            print(f"Buscando elemento..")
            self.base.doElementExistXpath(self.timeToWorkText)
            return True
    
    def getText(self)->str:
         return self.driver.find_element(By.XPATH, self.timeThisWeekText).text
