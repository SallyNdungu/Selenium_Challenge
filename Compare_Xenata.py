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
#accept cookies
accept_cookies = driver.find_element_by_css_selector("#hs-eu-confirmation-button").click()
#Navigate to compare Xenata link at the bottom of the page
compare_Xenata = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div[2]/div/div/div/span/div/ul/li[2]/a").click()
time.sleep(10)

#Prints the title of the loaded page
print(driver.title)

if driver.title == "Xeneta Products - Benchmark Container Freight Rates":
    print("Test Passed")
else:
    print("Test Failed")

#Close the open browser
driver.quit()
