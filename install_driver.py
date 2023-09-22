import requests
import sys
from zipfile import ZipFile
import os.path

def install_driver():

    print("Select OS to install Chromedriver for:")
    print("1. Windows 32-bit")
    print("2. Windows 64-bit")
    print("3. Linux")
    print("4. Mac arm64 (Apple Silicon)")
    print("5. Mac x86_64 (Intel)")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        platform = "win32"
    elif choice == "2":
        platform = "win64"
    elif choice == "3":
        platform = "linux64"
    elif choice == "4":
        platform = "mac-arm64"
    elif choice == "5":
        platform = "mac-x64"
    else:
        print("Invalid input. Exiting...")
        sys.exit()

    print("Downloading Chromedriver for " + platform + "...")

    url = "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE"
    r = requests.get(url=url)
    version = r.text

    print(f"Latest stable version: {version}")

    driver_url = f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{version}/{platform}/chromedriver-{platform}.zip"
    driver = requests.get(url=driver_url, allow_redirects=True)

    with open("chromedriver.zip", "wb") as f:
        f.write(driver.content)

    print("Extracting chromedriver.zip...")

    with ZipFile("chromedriver.zip", "r") as zipObj:
        zipObj.extractall()
    zipObj.close()

    print("Deleting chromedriver.zip...")
    os.remove("chromedriver.zip")

    print("Done!")

    if not os.path.exists("platform.txt"):
        save_platform(platform)


def save_platform(platform):
    with open("platform.txt", "w") as f:
        f.write(platform)

def get_platform():
    with open("platform.txt", "r") as f:
        return f.read()