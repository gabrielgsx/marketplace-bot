from selenium import webdriver
from time import sleep
import pyautogui
import os
from ads.Ad import titulo, preco, descricao, cidades
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from xpathss import title, price, category1, category2, condition1, condition2, description, color, tags, tags1, place, scroll_box
pyautogui.FAILSAFE = True

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\gabri\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 16")

browser = webdriver.Chrome('chromedriver.exe', chrome_options=options)

# For tabbing, arrow keys, and interacting with a single webpage
shortSleep = 0.2

# For all other loading, including file uploads, page refreshes or reloads, etc.
longSleep = 5


def postAllImages():
    sleep(2)
    pyautogui.moveTo(150, 400)
    sleep(1)
    for c in range(30):
        pyautogui.scroll(+100)
    images = getAdImagePaths()
    postImages(images[0])

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

def postImages(images):
    pyautogui.moveTo(150, 400)
    sleep(shortSleep)
    pyautogui.click()
    sleep(5)
    pyautogui.typewrite(images)
    sleep(shortSleep)
    pyautogui.press("enter")


def postAd():
    # for city in cidades:
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
    sleep(0.5)
    browser.find_element_by_xpath(f'{description}').send_keys(f'{descricao}')

    #TAGS
    sleep(1)
    browser.find_element_by_xpath(f'{tags}').send_keys(tags1)
    sleep(0.3)

    #PLACE
    browser.find_element_by_xpath(f'{place}').send_keys(Keys.CONTROL, 'a')
    browser.find_element_by_xpath(f'{place}').send_keys(Keys.DELETE)
    browser.find_element_by_xpath(f'{place}').send_keys('Manaus')   
    sleep(2)
    browser.find_element_by_xpath(f"//span[contains(text(),'Manaus')]").click()

    postAllImages()

    #FINISH
    sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[5]/div/div/div/div/div[1]/div/span').click()
    sleep(5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[5]/div[2]/div/div/div[1]/div/span').click()
def main():
    postAd()

main()

