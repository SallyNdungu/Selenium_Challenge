from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="/home/natalya/Documents/Drivers/geckodriver/geckodriver")
#open the Xenata demo page
driver.get("https://www.xeneta.com/demo")
driver.maximize_window()
print(driver.title)  #title of the page
#sleep command to allow the webpage load the page
time.sleep(45)
#decline cookies
decline_cookies = driver.find_element_by_css_selector("#hs-eu-decline-button").click()
time.sleep(10)
#Navigate to careers link at the bottom of the page
demo_careers = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[4]/div[2]/div/div/div/span/div/ul/li[1]/a").click()
time.sleep(30)
#close script window
driver.quit()