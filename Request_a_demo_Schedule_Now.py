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
time.sleep(10)
#click on the Schedule now link
schedule_now = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div/div/div/div/div/div/span/div[2]/div/div/p[2]/span/span/span/a").click()
time.sleep(10)
#Close the open browser
driver.quit()

