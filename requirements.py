import subprocess
from install_driver import install_driver

# Define required packages and their versions
with open("requirements.txt", "r") as required_packages:

    # Install required packages
    for package in required_packages:
        subprocess.check_call(["pip", "install", package])

install_driver()