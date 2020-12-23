#& C:/Users/Vikrant/Anaconda3/python.exe c:/Users/Vikrant/Documents/GitHub/Selenium-/Test.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

options = Options()
options.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(options=options,executable_path=PATH)

driver.get("https://www.sanfoundry.com/vhdl-questions-answers-eda-tools/")
print(driver.title)
print('\n')

#search = driver.find_element_by_name("s")
#search.send_keys("test")
#search.send_keys("test",Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inside-article"))
    )

    header = main.find_element_by_class_name("entry-content")

    print(header.text)
    
    print('\n')

finally:
    driver.quit()

