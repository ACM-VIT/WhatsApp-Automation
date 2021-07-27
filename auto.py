from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time
from config import CHROME_PROFILE_PATH


def numberOfMembers(group_name):
    options = webdriver.ChromeOptions()
    options.add_argument(CHROME_PROFILE_PATH)

    browser = webdriver.Chrome(options = options)

    browser.maximize_window()

    browser.get('https://web.whatsapp.com/')

    time.sleep(10)

    xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, xpath)))
    search_box.clear()

    pyperclip.copy(group_name)

    search_box.send_keys(Keys.SHIFT, Keys.INSERT)

    group_xpath = f'//span[@title="{group_name}"]'
    group_title = browser.find_element_by_xpath(group_xpath)

    group_title.click()

    top_xpath = f'(//span[@title="{group_name}"])[2]'
    top_click = browser.find_element_by_xpath(top_xpath)

    # print(top_click)
    top_click.click()

    number_xpath = '(//span[@class="_2MNpf VWPRY _1lF7t"])[3]' 
    number_of_part = browser.find_element_by_xpath(number_xpath)

    num = number_of_part.get_attribute('innerHTML')

    ans = int(num.partition(' ')[0])

    return ans


