**Project title**

Xenata Automation Challenge 

**Motivation**

The reason behind doing this challenge was 
1. Improve my chance of getting the job
2. Showing and proving to myself I am able to automate tests, that I can do it (and I did)

**How I prioritized what to automate:**

Xenata Demo Page

If I was interested in contacting Xenata for their services, I would focus on the following:
- Sign in Button (Assumption this is for repeat clients who have accounts?)
- Request a demo (dashboard) (A user would watch videos before reading up documentation)
    - Watch Videos
    - Schedule Now
    - Sign Up Here
- Compare Company - To allow the client to do due diligence
- Careers - If the user is interested in viewing potential roles open in the company
- Contact Us - Should always be working to ensure the client can reach out to the team

Xenata Careers Page

- Job title arrow link - Ensure the link drops to display the job details 
- Application Link - TO ensure the candidate is able to apply for the job 
A Global Tribe links - A potential candidate may want to view the teams and perks plus other details about the working culture and the links should be active to allow that.
    - Oslow, Norway
    - New York, USA
    - Hamburg, Germany 
Careers - Just in case the user clicks on the careers tab 


**Tech/framework used**

1. Selenium in Python - Automation Framework
2. PyCharm - IDE for building my scripts
3. GitHub - For saving my scripts 
4. Jenkins - For reports

**Code Example** 

Here is one of the scripts I created, it is very simple, using XPath, CSS selector and some other Identifiers. I would have preferred to use ID or name that way I can be guaranteed that should the webpage change, the elements can still be found. 

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox(executable_path="/home/natalya/Documents/Drivers/geckodriver/geckodriver")
#####open the Xenata demo page
driver.get("https://www.xeneta.com/careers")
driver.maximize_window()
print(driver.title)  #title of the page
#####sleep command to allow the webpage load the page
time.sleep(10)
#####accept cookies
careers_Accept_Cookies = driver.find_element_by_css_selector("#hs-eu-confirmation-button").click()
time.sleep(20)
#####A global tribe, Hamburg, Germany Link
hamburg_Germany_link = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/span/div[2]/div/div/div/div/div[2]/span/div[3]/div/div/div/a[2]").click()
time.sleep(30)

#####Prints the title of the loaded page
print(driver.title)

if driver.title == "Hamburg Careers":
    print("Test Passed")
else:
    print("Test Failed")

driver.quit()

**Installation** 

1. Operating system - Fedora 
2. PyCharm - Download Pycharm from the link below:
https://www.jetbrains.com/pycharm/download/#section=linux
3. Installing Python - Open your CMD (command line interface) and enter the commands below:
$ sudo apt-get update 
$ sudo apt-get install python3.6
4. Install Selenium: Open CMD and run the below command
pip install -U selenium
5. Install Selenium Webdrivers by navigating to the below websites and downloading the files that suit your operating system:

Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:	https://github.com/mozilla/geckodriver/releases
Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

6. Save the downloads in one folder (this is important when adding the path in the scripts)
e.g. I saved mine under Documents>>Drivers

7. Open PyCharm and create a project e.g. Xenata Challenge 
8. Click on File and navigate to Settings
9. Click on Project: Xenata Challenge >> Project Interpretor 
10. View the list of packages available and confirm selenium is part of the list. 
If it is, close the popup
If it is not, click on the + sign and search for Selenium, add it and close the pop up.
11. Link GItHub Account to PyCharm 
Click on Files>>Settings>>Version Control>>Click on the arrow next to Version Control>>Select GitHub
12. Log in to your GitHub account online and navigate to settings>>Developer Settings>>Personal Access Tokens
13. Generate a new token granting it all permissions and copy the generated Key
14. On PyCharm, from step 11, click on the + sign, in the pop up loaded, click on use token, enter the copied token in the field and click Ok.
15. On PyCharm, pull the code from GitHub to PyCharm and run. Expected results, successes fro each test case executed. 
16. Integrate Jenkins with GitHub to generate selenium reports
Click on this link for a detailed guide on how to set-up, install Jenkins 
https://www.jenkins.io/doc/book/installing/linux/#fedora 
I did not complete this set up as I got errors, next target is to integrate GitHub with Jenkins.

**Challenge:**
1. Locating elements using name - 
Using name would ensure that when the webpages are updated, the scripts will still work as they will be locating the name as opposed to Xpath or CSS Selector which change with updates requiring constant update of the scripts. 
With my scripts, should elements change, the scripts will fail. 
Since I was not able to locate elements using the name elements that do not change, I introduced the if else statement to confirm that the loaded page is the expected one. 

Thank you!