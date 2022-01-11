from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui
import pyperclip
import os
from ads.Ad import *
from xpathss import *

pyautogui.FAILSAFE = True

profile = FirefoxProfile("C:\\Users\\gabri\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\em4skdsw.default-release")
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
    input_box.send_keys(f'{descricao10}'+ Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao11}'+ Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao12}'+ Keys.SHIFT + Keys.ENTER + Keys.ENTER)
    input_box.send_keys(f'{descricao13}'+ Keys.SHIFT + Keys.ENTER)

def postAllImages(cont):
    sleep(2)
    pyautogui.moveTo(200, 400)
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
    ##
    pyperclip.copy(images[cont])
    pyautogui.hotkey("ctrl", "v")
    print("\033[92m {}\033[00m" .format(images[cont]))
    #
    sleep(3)
    pyautogui.press("enter")
    sleep(3)
    #
    pyautogui.moveTo(150, 400)
    sleep(0.2)
    pyautogui.click()
    sleep(3)
    ##
    pyperclip.copy(images[1+cont])
    pyautogui.hotkey("ctrl", "v")
    print("\033[92m {}\033[00m" .format(images[1+cont]))
    #
    sleep(3)

    pyautogui.press("enter")
    sleep(3)
    ##
    #
    pyautogui.moveTo(250, 400)
    sleep(0.2)
    pyautogui.click()
    sleep(3)
    ##
    pyperclip.copy(images[2+cont])
    pyautogui.hotkey("ctrl", "v")
    print("\033[92m {}\033[00m" .format(images[2+cont]))
    #
    sleep(3)
    pyautogui.press("enter")
    sleep(3)
    pyautogui.press("esc")
    # os.rename(f"D:\\backup\\desktop\\projetos\\triturador\\ads\\{cont+1}.jpg", f"D:\\backup\\desktop\\projetos\\triturador\\ads\\__pycache__\\{cont+1}.jpg")
    # sleep(1)
    # os.rename(f"D:\\backup\\desktop\\projetos\\triturador\\ads\\{cont+2}.jpg", f"D:\\backup\\desktop\\projetos\\triturador\\ads\\__pycache__\\{cont+2}.jpg")
    sleep(3)


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
    
    images.sort(key=lambda x: int(x[54:].replace('.jpg', '')))
    return images


def postAd(cont):
    while True:
        for city in cidades:
                try:
                    sleep(10)
                    browser.get('https://www.facebook.com/marketplace/create/item')
                    sleep(8)

                    #LOAD THE ELEMENTS
                    sleep(2)
                    pyautogui.moveTo(150, 400)
                    sleep(2)
                    for c in range(30):
                        pyautogui.scroll(-100)

                    sleep(8)
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

                    sleep(5.5)
                    browser.find_element_by_xpath(f'{condition2}').click()

                    #DESCRIPTION
                    postDescription()

                    #TAGS
                    sleep(6)
                    browser.find_element_by_xpath(f'{tags}').send_keys(tags2)
                    sleep(0.3)

                    #PLACE
                    browser.find_element_by_xpath(f'{place}').send_keys(Keys.CONTROL, 'a')
                    browser.find_element_by_xpath(f'{place}').send_keys(Keys.DELETE)
                    browser.find_element_by_xpath(f'{place}').send_keys(f'{city}') 

                    sleep(2)
                    browser.find_element_by_xpath(f"//span[contains(text(),'{city}')]").click()
                    sleep(1)
                    print("\033[92m {}\033[00m" .format(city))
                    postAllImages(cont)
                    cont += 3

                    #FINISH
                    sleep(4)
                    browser.find_element_by_xpath(f'{finish1}').click()
                    sleep(5)
                    browser.find_element_by_xpath(f'{finish2}').click()
                
                    #browser.refresh
                except:
                    continue
                if city == 'Carapicuíba':
                    break

def main(cont):
    postAd(cont)

main(cont)
