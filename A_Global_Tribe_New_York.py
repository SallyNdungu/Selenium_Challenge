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
#accept cookies
careers_Accept_Cookies = driver.find_element_by_css_selector("#hs-eu-confirmation-button").click()
time.sleep(20)
#A global tribe, New York, USA
new_York = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[2]/div/div/div/div/div[2]/span/div[2]/div/a/div").click()
time.sleep(30)

#Prints the title of the loaded page
print(driver.title)

if driver.title == "New York City Careers":
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()