from selenium import webdriver
from time import sleep

username = ''
password = ''

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=User") # IT WILL CREATE A "USERS" FOLDER THAT WILL HOLD YOUR INSTAGRAM USER COOKIE

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)


def LogIn():
    driver.get("https://www.instagram.com/accounts/login/")
    sleep(2)
    driver.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(username)
    driver.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(password)
    driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()
    sleep(6)
    driver.find_element_by_xpath("//button[contains(text(), 'Not now')]")\
        .click()
    sleep(2)
    driver.find_element_by_xpath("//button[contains(text(), 'Not now')]")\
        .click()
    sleep(2)

LogIn(username, password)
