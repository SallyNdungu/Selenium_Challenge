from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="/home/natalya/Documents/Drivers/geckodriver/geckodriver")
#open the Xenata demo page
driver.get("https://www.xeneta.com/careers")
driver.maximize_window()
print(driver.title)  #title of the page
#sleep command to allow the webpage load the page
time.sleep(5)
#Click on the request a demo link
careers_pop_up = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/span/div[2]/ul/li[6]/a").click()
time.sleep(5)
#click on the Group Live Demo link
careers_group_live_demo = driver.find_element_by_id("cta_button_1816946_2b2944d5-4dbd-437d-9654-65d8de7d141f").click()
time.sleep(10)
#Close the open browser
driver.quit()