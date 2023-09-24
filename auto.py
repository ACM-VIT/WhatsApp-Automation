from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time
from config import CHROME_DRIVER_PATH, CHROME_PATH
import os
from prettytable import PrettyTable

def numberOfMembers(groups):
    os.environ['PATH'] += os.pathsep + CHROME_DRIVER_PATH

    options = webdriver.ChromeOptions()
    options.binary_location = CHROME_PATH

    browser = webdriver.Chrome(CHROME_DRIVER_PATH, chrome_options=options)

    browser.maximize_window()

    browser.get('https://web.whatsapp.com/')

    time.sleep(10)

    xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, xpath)))
    
    res = []
    for group_name in groups:
        search_box.click()  # Click the div to ensure it has focus
        
        pyperclip.copy(group_name)

        search_box.send_keys(Keys.SHIFT, Keys.INSERT)
        search_box.click()
        search_box.send_keys(Keys.ENTER)

        clear_button = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/span/button')))
        clear_button.click()

        top_xpath = '//*[@id="main"]/header/div[2]/div[1]/div/span'

        top_click = WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, top_xpath)))
        top_click.click()
        time.sleep(3)

        number_xpath = '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/div/section/div[1]/div/div[3]/span/span/button' # complete Xpath of the element that contains number of participants.
        number_of_part = WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, number_xpath)))

        num = number_of_part.get_attribute('innerHTML')

        ans = int(num.split(' ')[0])

        res.append(ans)
    return res

def get_members_info(group_name):
    os.environ['PATH'] += os.pathsep + CHROME_DRIVER_PATH

    browser = webdriver.Chrome(CHROME_DRIVER_PATH)
    browser.maximize_window()
    browser.get('https://web.whatsapp.com/')
    time.sleep(10)

    # search group
    search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
    click_on(browser, search_box_xpath)
    pyperclip.copy(group_name)
    search_box.send_keys(Keys.SHIFT, Keys.INSERT)
    click_on(browser, search_box_xpath)
    search_box.send_keys(Keys.ENTER)

    click_on(browser, '//*[@id="main"]/header/div[2]/div[1]/div/span')
    time.sleep(10)

    number_xpath = '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/div/section/div[1]/div/div[3]/span/span/button' # complete Xpath of the element that contains number of participants.
    number_of_part = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, number_xpath)))

    num = number_of_part.get_attribute('innerHTML')

    total_participants = int(num.split(' ')[0])

    # create table
    table = PrettyTable()
    table.field_names = ["Sr. No.", "Name", "Mobile No."]

    # get self's mobile number & add it to table
    my_mobile_xpath = '//*[@id="pane-side"]/div/div/div/div[1]/div/div/div[2]/div[2]/div[2]/span[1]/span'
    my_mobile_element = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, my_mobile_xpath)))
    table.add_row([1, "You", my_mobile_element.get_attribute('innerHTML')])

    if total_participants > 10:
        table.add_rows(getParticipantsInfo(browser, 10, 2, 1, 1))
        table.add_rows(getParticipantsInfo(browser, total_participants, 10, 9, 1))

    else:
        table.add_rows(getParticipantsInfo(browser, total_participants, 2, 1, 0))

    return table

def getParticipantsInfo(browser, start, end, count, moreThan10):
    rows = []
    for i in range(start, end, -1):
        # if there are more than 10 participants then click on more
        if (moreThan10):
            click_on(browser, '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/div/section/div[6]/div[2]/div[2]')
        
        # increment count
        count += 1

        # open participant's info
        click_on(browser, '//*[@id="pane-side"]/div/div/div/div[' + str(i) + ']/div')
        time.sleep(5)

        # get text1 of the participant
        text1_xpath = '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[2]/h2/span'
        text1_element = WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, text1_xpath)))
        text1 = text1_element.get_attribute('innerHTML')

        # check if text2 is present or not
        text2_xpath = '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/section/div[1]/div[2]/div/span/span'

        # check if the element is present or not
        if browser.find_elements_by_xpath(text2_xpath):
            # get text2
            text2_element = WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, text2_xpath)))
            text2 = text2_element.get_attribute('innerHTML')

            # this is done b'coz if the person's contact is not saved then the context of both elements appear swapped
            if text2[0] == '~':
                name = text2[1:]
                mobile = text1
            else:
                name = text1
                mobile = text2

            # add participant's info to table
            rows.append([count, name, mobile])

        else:
            # add participant's info to table
            rows.append([count, "", text1])
        
        # click on back button
        click_on(browser, '//*[@id="app"]/div/div/div[6]/span/div/span/div/header/div/div[1]/div/span')

    return rows

def click_on(browser, xpath):
    WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, xpath))).click()