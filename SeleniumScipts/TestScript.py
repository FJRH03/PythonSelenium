# Import Selenium WebDriver
__author__ = 'Francisco Ramirez'

import time
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\dev tools\geckodriver.exe') #Set the path of your binary file here

#Set up webdriver
driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(20)
driver.implicitly_wait(20)

#Get URL
driver.get("https://www.facebook.com");

#Find elements from facebook webpage
driver.find_element_by_class_name('inputtext').send_keys('myuser@mail.com')
driver.find_element_by_id('pass').send_keys('password')
driver.find_element_by_id('u_0_a').click()

#Take a Screenshot
driver.get_screenshot_as_file(".\\Screenshots\\Facebook.png")

#Delay 5 second and then Close webdriver
time.sleep(5)
driver.close()
driver.quit()


