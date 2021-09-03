"""
Main function for MiniCarWale
"""
import cars
import re
print("\n" + "--Welcome to Mini CarWale--" + "\n")
print("Choose Your Car and get more details")
print("View Price Breakup and EMI Calculations" + "\n")
print("-- Please Signup to enter Minicarwale --")
mailid = input("Enter your gmail ID     : ")
phone = input("Enter your phone number : ")
if re.match("[a-z A-Z 0-9]+@gmail.com$", mailid) and re.match("[0-9]{10}",phone):
    text_file = open("data.txt", "a")
    text_file.writelines(mailid)
    text_file.writelines("\n")
    text_file.writelines(phone)
    text_file.writelines("\n")
    text_file.writelines("\n")
    text_file.close()
    print("Choose Brand of your Car")
    print("1. TATA" + "\n" + "2. Maruti" + "\n" + "3. Skoda" + "\n" + "4. Honda" + "\n" + "5. Hyundai")
    CHOICE = int(input("Enter your choice : "))
    cars.totalcars(CHOICE)
else:
    print("Give valid details")
