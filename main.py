import os
from config import CHROME_DRIVER_PATH
from selenium import webdriver
import time

os.environ['PATH'] += os.pathsep + CHROME_DRIVER_PATH
browser = webdriver.Chrome(CHROME_DRIVER_PATH)
browser.maximize_window()
browser.get('https://web.whatsapp.com/')
time.sleep(10)

from tabulate import tabulate
from auto import numberOfMembers, get_members_info, send_on_whatsapp

# change num to 1, 2, or 3 to run the respective code
num = 3

# 1. Get number of participants in each group
if num == 1:
    # Insert your group names here
    groups = ["Group 1", "Group 2"]

    head = ["Group Name", "Number of Participants"]
    members = numberOfMembers(browser, groups)

    data = []
    for i in range(len(groups)):
        data.append([groups[i], members[i]])

    print(tabulate(data, headers=head, tablefmt="github"))

# 2. Print participants' info
elif num == 2:
    # Insert your group name here
    print(get_members_info(browser, "Group Name"))

# 3. Send group info to WhatsApp
elif num == 3:
    # Insert your group name here
    group_name = "Testing"

    result1 = "*Number of participants in Group:* " + str(numberOfMembers(browser, [group_name])[0])

    table = get_members_info(browser, group_name)

    result2 = "*List of participants:*\n```" + table.get_string().replace("You", "Me ") + "```"

    send_on_whatsapp(browser, result1 + "\n\n" + result2)