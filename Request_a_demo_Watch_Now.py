from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="/home/natalya/Documents/Drivers/geckodriver/geckodriver")
#open the Xenata demo page
driver.get("https://www.xeneta.com/demo")
driver.maximize_window()
print(driver.title)  #title of the page
#sleep command to allow the webpage load the page
time.sleep(5)
#Click on the request a demo link
pop_up = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/span/div[2]/ul/li[6]/a").click()
time.sleep(5)
#click on the Watch now link
watch_now = driver.find_element_by_id("cta_button_1816946_180bbc25-62fd-4a6b-8e02-5c22aba5c82f").click()
time.sleep(10)

#Prints the title of the loaded page
print(driver.title)

if driver.title == "Watch Xeneta Videos":
    print("Test Passed")
else:
    print("Test Failed")

#Close the open browser
driver.quit()