from selenium import webdriver
import sys
import time

__author__ = 'Francisco Ramirez'


#1. You must have initialized your selenium server: java -jar selenium-server-standalone-3.141.59.jar

#Set your host:port/wd/hub
driver = webdriver.Remote(desired_capabilities= webdriver.DesiredCapabilities.FIREFOX, command_executor='http://127.0.0.1:4444/wd/hub')

#webdriver manage and set-up
driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(20)
driver.implicitly_wait(20)

#Driver goes to Google
driver.get("http://www.google.com")
print('Driver on: ', driver.title)

element = driver.find_element_by_name('q')
element.send_keys('Hello from Selenium')
element.submit()

#Driver take a screenshot
driver.get_screenshot_as_file(".\\Screenshots\\Google.png")


#Driver delay and then close
time.sleep(5)
driver.close()

print('\n--Demo Remote Controller Selenium finished --')