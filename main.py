from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui
import os
from ads.Ad import *
from xpathss import *

pyautogui.FAILSAFE = True

profile = FirefoxProfile("C:\\Users\\gabri\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\l0tmvkmi.default-release")
browser = webdriver.Firefox(profile)

wait = WebDriverWait(browser, 10)

cont = 0

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
    input_box.send_keys(f'{descricao11}'+ Keys.SHIFT + Keys.ENTER)

def postAllImages(cont):
    sleep(2)
    pyautogui.moveTo(150, 400)
    sleep(1)
    for c in range(30):
        pyautogui.scroll(+100)
    images = getAdImagePaths()
    postImages(images, cont)

def postImages(images, cont):
    pyautogui.moveTo(150, 400)
    sleep(0.2)
    pyautogui.click()
    sleep(5)
    pyautogui.typewrite(images[cont])
    print(images[cont])
    sleep(0.5)
    pyautogui.press("enter")
    sleep(0.5)
    #
    pyautogui.moveTo(150, 400)
    sleep(0.2)
    pyautogui.click()
    sleep(3)
    #
    pyautogui.typewrite(images[1+cont])
    print(images[1+cont])
    pyautogui.press("enter")
    
    sleep(0.5)

def getAdImagePaths():
    ads = os.getcwd() + "/ads/"
    files = os.listdir(ads)

    images = []
    for file in files:
        if file[0] != "." and file != "Ad.py" and file != "__pycache__":
            #images.append(ads + file)
            x = ads + file
            for c in x:
                if c == '/':
                    valores = x.replace('/', "\\")
            images.append(valores)

    images.sort(key=lambda x: int(x[48:].replace('.jpg', '')))
    return images

def postAd(cont):
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
        sleep(6)
        browser.find_element_by_xpath(f'{tags}').send_keys(tags1)
        sleep(0.3)

        #PLACE
        browser.find_element_by_xpath(f'{place}').send_keys(Keys.CONTROL, 'a')
        browser.find_element_by_xpath(f'{place}').send_keys(Keys.DELETE)
        browser.find_element_by_xpath(f'{place}').send_keys(f'{city}')   
        sleep(2)
        browser.find_element_by_xpath(f"//span[contains(text(),'{city}')]").click()

        postAllImages(cont)
        cont += 2

        #FINISH
        sleep(1)
        browser.find_element_by_xpath(f'{finish1}').click()
        sleep(5)
        browser.find_element_by_xpath(f'{finish2}').click()


def main(cont):
    postAd(cont)

main(cont)
