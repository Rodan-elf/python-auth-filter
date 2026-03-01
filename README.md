# Python Auth Filter (Beginner Level)
> **Security project completed during the Google Cybersecurity Professional Certificate.**
> *Focus: Using Python basics to manage a simple access control list.*

---

## 1. Project Description
This project solves a simple security problem: managing a list of authorized IP addresses for a healthcare company. 

When employees leave or change roles, their access must be removed to maintain security. I wrote a basic Python script to automate this task, which helps prevent unauthorized access to sensitive patient data and ensures that only current staff can enter the restricted subnetwork.

---

## 2. How the Script Works (Step-by-Step)

### Step 1: Opening the File
The script starts by identifying the file `rodan_allow_list.txt`. I use the `with` statement because it is the safest way to open a file in Python; it makes sure the file closes automatically when the script finishes, preventing any data loss.

### Step 2: Reading the IPs
The script reads the file and converts the content into a **string** (a block of text) so the program can process the data.

### Step 3: Working with a List
To make it easier to remove specific IPs, I convert that string into a **list** using the `.split()` method. This turns each IP address into an individual item that Python can easily identify.

### Step 4: Removing Unauthorized Access
I use a `for` loop to go through a "remove list" containing IPs that no longer need access. For every IP in that list, the script checks if it exists in our allow list. If it is found, the script removes it from the list.

### Step 5: Updating the File
Finally, I convert the updated list back into text and write it back into the `rodan_allow_list.txt` file. This replaces the old list with the new, secure version.

---

## 3. Simple Python Code
```python
# Simple algorithm to update an allow list of IP addresses
# Created for the Google Cybersecurity Certificate

# 1. Define the file name and the IPs to be removed
import_file = "rodan_allow_list.txt"
remove_list = ["192.168.1.10", "192.168.1.25", "10.0.0.15"] 

# 2. Open the file and read the content
with open(import_file, "r") as file:
    ip_addresses = file.read()

# 3. Convert the text into a list
ip_addresses = ip_addresses.split()

# 4. Loop through the remove_list to find and delete IPs
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# 5. Convert the list back to text and save the file
ip_addresses = "\n".join(ip_addresses)
with open(import_file, "w") as file:
    file.write(ip_addresses)

print("Update finished: Unauthorized IPs have been removed.")
