from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui
import os
from ads.Ad import titulo, preco, descricao1, descricao2, descricao3, descricao4, descricao5, descricao6,  descricao7,  descricao8, descricao9, descricao10, cidades
from xpathss import title, price, category1, category2, condition1, condition2, description, color, tags, tags1, place, finish1, finish2, scroll_box

pyautogui.FAILSAFE = True

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Your\\Path\\Here")

#FIREFOX BROWSER
#profile = FirefoxProfile("C:\\Your\\Path\\Here")
#browser = webdriver.Firefox(profile)

browser = webdriver.Chrome('chromedriver.exe', chrome_options=options)
wait = WebDriverWait(browser, 10)

# For tabbing, arrow keys, and interacting with a single webpage
shortSleep = 0.2

# For all other loading, including file uploads, page refreshes or reloads, etc.
longSleep = 5


def postDescription():
    sleep(2)
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, description)))
    input_box.send_keys(f'{descricao1}' + Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao2}' + Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao3}' + Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao4}'+ Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao5}' + Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao6}' + Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao7}' + Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao8}'+ Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao9}'+ Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao10}'+ Keys.SHIFT + Keys.ENTER + Keys.ENTER)

def postAllImages():
    sleep(2)
    pyautogui.moveTo(150, 400)
    sleep(1)
    for c in range(30):
        pyautogui.scroll(+100)
    images = getAdImagePaths()
    postImages(images[0])

def postImages(images):
    pyautogui.moveTo(150, 400)
    sleep(shortSleep)
    pyautogui.click()
    sleep(5)
    pyautogui.typewrite(images)
    sleep(shortSleep)
    pyautogui.press("enter")


def getAdImagePaths():
    ads = os.getcwd() + "/ads/"
    files = os.listdir(ads)

    images = []
    for file in files:
        if file[0] != "." and file != "Ad.py":
            #images.append(ads + file)
            x = ads + file
            for c in x:
                if c == '/':
                    valores = x.replace('/', "\\")
            images.append(valores)
    return images

def postAd():
    for city in cidades:
        sleep(10)
        browser.get('https://www.facebook.com/marketplace/create/item')
        sleep(5)

        #LOAD THE ELEMENTS
        sleep(2)
        pyautogui.moveTo(150, 400)
        sleep(1)
        for c in range(30):
            pyautogui.scroll(-100)

        sleep(2)
        #TITLE
        browser.find_element_by_xpath(f'{title}').send_keys(f'{titulo}')

        #PRICE
        browser.find_element_by_xpath(f'{price}').send_keys(f'{preco}')

        #CATEGORY
        sleep(5)
        browser.find_element_by_xpath(f'{category1}').click()

        sleep(3)
        browser.find_element_by_xpath(f'{category2}').click()

        #CONDITION
        sleep(5)
        browser.find_element_by_xpath(f'{condition1}').click()

        sleep(5)
        browser.find_element_by_xpath(f'{condition2}').click()

        #DESCRIPTION
        postDescription()

        #TAGS
        sleep(1)
        browser.find_element_by_xpath(f'{tags}').send_keys(tags1)
        sleep(0.3)

        #PLACE
        browser.find_element_by_xpath(f'{place}').send_keys(Keys.CONTROL, 'a')
        browser.find_element_by_xpath(f'{place}').send_keys(Keys.DELETE)
        browser.find_element_by_xpath(f'{place}').send_keys(f'{city}')   
        sleep(2)
        browser.find_element_by_xpath(f"//span[contains(text(),'{city}')]").click()

        postAllImages()

        #FINISH
        sleep(1)
        browser.find_element_by_xpath(f'{finish1}').click()
        sleep(5)
        browser.find_element_by_xpath(f'{finish2}').click()


def main():
    postAd()

main()

