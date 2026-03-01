# Project: Automated ACL Update Algorithm
# Framework: Google Cybersecurity Professional Certificate

import_file = "rodan_allow_list.txt"
remove_list = ["192.168.1.10", "192.168.1.25", "10.0.0.15"] 

# Step 1: Open the file and read the content
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Step 2: Convert the text into a list
ip_addresses = ip_addresses.split()

# Step 3: Loop through the remove_list to find and delete IPs
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Step 4: Convert the list back to text and save the file
ip_addresses = "\n".join(ip_addresses)
with open(import_file, "w") as file:
    file.write(ip_addresses)

print("Update finished: Unauthorized IPs have been removed.")
