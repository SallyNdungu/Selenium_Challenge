from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="/home/natalya/Documents/Drivers/geckodriver/geckodriver")
#open the Xenata demo page
driver.get("https://www.xeneta.com/careers")
driver.maximize_window()
print(driver.title)  #title of the page
#sleep command to allow the webpage load the page
time.sleep(10)
#decline cookies
careers_decline_cookies = driver.find_element_by_css_selector("#hs-eu-decline-button").click()
time.sleep(20)
#A global tribe, Oslow, Norway link
oslow_norway_link = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[2]/div/div/div/div/div[2]/span/div[1]/div/div/div/a[2]").click()
time.sleep(30)

#Prints the title of the loaded page
print(driver.title)

if driver.title == "Oslo Careers":
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()