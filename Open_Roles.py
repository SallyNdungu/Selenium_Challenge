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
#Open roles - select one open role
test_Automation_Drop_Down = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[3]/div/div/div/div/div/div[3]/div/div[1]/div/h4").click()
time.sleep(25)
#Close drop down
driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[3]/div/div/div/div/div/div[3]/div/div[1]/div/h4").click()
time.sleep(25)
#Open roles - select another one open role
VP_Product_Drop_Down = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/h4").click()
time.sleep(25)
#Apply link
VP_Product_Apply_Here = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[1]/p[39]/a").click()
time.sleep(15)
