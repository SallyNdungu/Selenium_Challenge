from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="/home/natalya/Documents/Drivers/geckodriver/geckodriver")

driver.get("https://www.xeneta.com/demo")

print(driver.title)  #title of the page

driver.close()