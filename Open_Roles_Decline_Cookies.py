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
careers_Decline_Cookies = driver.find_element_by_css_selector("#hs-eu-decline-button").click()
time.sleep(20)
#Open roles - select one open role
technical_Content_Drop_Down = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[3]/div/div/div/div/div/div[4]/div/div[1]/div/h4").click()
time.sleep(25)
#Close drop down
driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[3]/div/div/div/div/div/div[4]/div/div[1]/div/h4").click()
time.sleep(25)
#Open roles - select another one open role
open_Application_Drop_Down = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[3]/div/div/div/div/div/div[5]/div/div[1]/div/h4").click()
time.sleep(25)
#Apply link
open_Application_Apply_Here = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[3]/div/div/div/div/div/div[5]/div/div[2]/div[1]/p[10]/a/span").click()
time.sleep(15)
#Prints the title of the loaded page
print(driver.title)

if driver.title == "Careers":
    print("Test Passed")
else:
    print("Test Failed")
