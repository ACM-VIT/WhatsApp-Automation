import os
from config import CHROME_DRIVER_PATH
from selenium import webdriver
import time

from tabulate import tabulate
from auto import numberOfMembers, get_members_info, send_on_whatsapp

print("\nHi, What do you want?")
print("  Enter 1 to get number of participants in groups.\n  Enter 2 to get details of members of a group.")
choice = input("Enter your choice: ")

print("\nOk, How do you want the output?")
print("  Enter 1 to print on the terminal.\n  Enter 2 to send on WhatsApp group.")
output_choice = input("Enter your choice: ")

output = ""
groups = []
group_name = ""

def create_browser():
    os.environ['PATH'] += os.pathsep + CHROME_DRIVER_PATH
    browser = webdriver.Chrome(CHROME_DRIVER_PATH)
    browser.maximize_window()
    browser.get('https://web.whatsapp.com/')
    time.sleep(10)
    return browser

match choice:
    # 1. Get number of participants in each group
    case "1":
        print("\nEnter the name of each group & press enter. (Enter X to stop)")
        while True:
            group = input("Enter: ")
            if group == "X" or group == "x":
                break
            groups.append(group)
        
        browser = create_browser()
        table_head = ["Group Name", "Number of Participants"]
        members = numberOfMembers(browser, groups, output_choice)

        data = []
        for i in range(len(groups)):
            data.append([groups[i], members[i]])
        
        output = tabulate(data, headers=table_head, tablefmt="github")

    # 2. Get details of each participant of the group
    case "2":
        group_name = input("Enter group name: ")
        browser = create_browser()
        output = get_members_info(browser, group_name)
    
    case _:
        print("Invalid choice")

match output_choice:
    case "1":
        print(output)

    case "2":
        if (choice == "2"):
            result1 = "*Number of participants in Group:* " + str(numberOfMembers(browser, [group_name])[0])
            result2 = "*List of participants:*\n```" + output.get_string() + "```"
            send_on_whatsapp(browser, result1 + "\n\n" + result2)
    
    case _:
        print("Invalid choice")