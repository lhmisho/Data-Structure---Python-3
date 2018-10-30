import re

with open('file.txt', 'r') as f:
    text = f.read()

#print(text)

# we can get all the line from file.text useing re

# one way
match = re.findall(r'^.*?$',text, re.MULTILINE)  # this will return none
#print(match)

# in this case it will return a empty sting

match = re.findall(r'^.+?$', text, re.MULTILINE)
#print(match)

# suppose we have some line like <li> ... </li> we can retrive the value
s = "<li>Raihan</li><li>Roman</li><li>Misho</li>"
match = re.findall(r'<li>(.*?)</li>', text, re.MULTILINE)
#print(match)

text = "This is line 1. Date is 2017/06/01. And there is another date: 2017-07-01. The third and final date is 2017/08/30"

patern = re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')
match = patern.findall(text)
print(match)




