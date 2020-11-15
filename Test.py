from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(options=options,executable_path=PATH)

driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()
