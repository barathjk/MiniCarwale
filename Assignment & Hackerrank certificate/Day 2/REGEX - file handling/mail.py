"""
Mail ID validation using REGEX
"""
import re
FILE = open("mail.txt", "r+")
next(FILE)
for mailids in FILE:
    if re.match("[a-z A-Z 0-9]+@gmail.com$", mailids):
        print("Valid")
    else:
        print("Not valid")
FILE.close()
