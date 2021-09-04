"""
Userdefined String validation using REGEX
"""
import re
FILE = open("userdefined.txt", "r")
print(re.findall("Coimbatore", FILE.readline()))
print(re.search("gmail", FILE.readline()))
print(re.match("ltts", FILE.readline()))
FILE.close()
