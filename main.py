import subprocess

# Run the requirements.py script to install required packages
subprocess.check_call(["python", "requirements.py"])

from auto import numberOfMembers
import subprocess

subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

groups = ["ACM Research Formal Group","ACM Board Technical","ACM-VIT | INFORMAL"]
#Insert your group names here

print(numberOfMembers(groups))

