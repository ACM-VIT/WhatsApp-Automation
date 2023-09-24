from tabulate import tabulate
from auto import numberOfMembers, get_members_info

# change num to 1 or 2 to run the respective code
num = 2

# 1. Get number of participants in each group
if num == 1:
    # Insert your group names here
    groups = ["Group 1", "Group 2"]

    head = ["Group Name", "Number of Participants"]
    members = numberOfMembers(groups)

    data = []
    for i in range(len(groups)):
        data.append([groups[i], members[i]])

    print(tabulate(data, headers=head, tablefmt="github"))

# 2. Get participants' info
elif num == 2:
    # Insert your group name here
    print(get_members_info("Group Name"))