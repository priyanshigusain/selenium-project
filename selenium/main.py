from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from info import LoginId, password
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.netflix.com/in/login")
# username(before importing write your login id and password in info.py file)
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input').send_keys(LoginId)

# password
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input').send_keys(password)

# signin
driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').click()
# profile Selection
time.sleep(2)
# instead of profile_name enter your own profile_name
driver.find_element_by_link_text('profile_name').click()
time.sleep(3)

# instead of recent watched show here your own currently watching show
driver.find_element_by_link_text('recent watched show here').click()
driver.find_element_by_link_text('Resume').click()
