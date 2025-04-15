from selenium import webdriver

cService = webdriver.ChromeService(executable_path='C:\Program Files (x86)\chromedriver.exe')
driver = webdriver.Chrome(service = cService)

driver.get("https://techwithtim.net")
print(driver.title)