import re

def mobileNumber(number):
    pattern = re.compile(r"(\+[0-9]{1,3}[\s-]?)?[0]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}")
    matches = pattern.finditer(str(number))
    for x in matches :
        print("Found Valid Mobile Number : ",x)
    
