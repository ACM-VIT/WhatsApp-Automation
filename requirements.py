import subprocess

# Define the required packages and their versions
required_packages = [
    "pyperclip==1.8.2",
    "selenium==3.141.0",
    "urllib3==1.26.6",
]

# Install the required packages
for package in required_packages:
    subprocess.check_call(["pip", "install", package])

