"""
Main function for MiniCarWale
"""
import re
import cars

print("\n" + "--Welcome to Mini CarWale--" + "\n")
print("Choose Your Car and get more details")
print("View Price Breakup and EMI Calculations" + "\n")
print("-- Please Signup to enter Minicarwale --")
MAILID = input("Enter your gmail ID     : ")
PHONE = input("Enter your PHONE number : ")
if re.match("[a-z A-Z 0-9]+@gmail.com$", MAILID) and re.match("[0-9]{10}", PHONE):
    TEXT = open("data.txt", "a")
    TEXT.writelines(MAILID)
    TEXT.writelines("\n")
    TEXT.writelines(PHONE)
    TEXT.writelines("\n")
    TEXT.writelines("\n")
    TEXT.close()
    print("Choose Brand of your Car")
    print("1. TATA" + "\n" + "2. Maruti" + "\n" + "3. Skoda")
    print("4. Honda" + "\n" + "5. Hyundai")
    CHOICE = int(input("Enter your choice : "))
    cars.totalcars(CHOICE)
else:
    print("Give valid details")
