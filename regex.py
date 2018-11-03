import re

text = "Multiple phone number: 016 856634198, 01711111111, 01685-634198, 00000000000, 123-321"

match = re.findall(r'01[56789]\s*\d{2}\s*\d{6}',text)

country = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden , Switzweland"

li = re.findall(r'(\w+lands*)', country)


find = re.search('bangla', 'Bangladesh', re.IGNORECASE)
#print(find.group())

s = "Bangladesh is our homeland"
match = re.search('B.n', s)

match = re.search('o\w\w', s)
match = re.search('i\w+', s)
match = re.search('B\w.+h', s)
match = re.search('B\w.+?h', s)

#print(match)

###############################################################
number = re.compile(r'01[56789]\s*\d{2}\s*\d{6}', re.IGNORECASE)
phone = '0168563419822'

rng = 11
phone_range = len(phone)
if phone_range <= rng:
    if number.match(phone):
        print(True)
    else:
        print(False)
else:
    print("Range over")