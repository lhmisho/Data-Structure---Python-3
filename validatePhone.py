import re

def validNumber(phone_nuber):
    pattern = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
    return pattern.match(phone_nuber) is not None

phone = validNumber('01685634198')
print(phone)