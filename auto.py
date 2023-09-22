from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time
from config import CHROME_DRIVER_PATH
import os


def numberOfMembers(groups):
    os.environ['PATH'] += os.pathsep + CHROME_DRIVER_PATH

    browser = webdriver.Chrome(CHROME_DRIVER_PATH)

    browser.maximize_window()

    browser.get('https://web.whatsapp.com/')

    time.sleep(10)

    xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, xpath)))
    
    res = []
    for group_name in groups:
        search_box.click()  # Click the div to ensure it has focus
        
        search_box.clear()  # This line clears the search box
        
        pyperclip.copy(group_name)

        search_box.send_keys(Keys.SHIFT, Keys.INSERT)
        search_box.click()
        search_box.send_keys(Keys.ENTER)

        top_xpath = '//*[@id="main"]/header/div[2]/div[1]/div/span'

        top_click = WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, top_xpath)))
        top_click.click()
        time.sleep(3)

        # Issue #6
        number_xpath = "" # complete Xpath of the element that contains number of participants.
        number_of_part = WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, number_xpath)))

        num = number_of_part.get_attribute('innerHTML')

        ans = int(num.split(' ')[0])

        res.append(ans)
    return res