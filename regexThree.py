import re
dates = "this line will contain some dates. those are 2018/10/31 and 2018-08-23"

pattern = re.compile(r'(\d{4})[-/](\d{2})[-/](\d{2})')
#import pdb; pdb.set_trace()
result = pattern.findall(dates)
#print(result)

names = "<li>Raihan</li><li>Roman</li><li>Misho</li>"
result = re.findall(r'<li>(.*?)</li>', names)
#import pdb; pdb.set_trace()


## use of sub

s = "Abcd 123-342"

result = re.sub(r'\d', '0', s)

with open('player.html','r') as f:
    text = f.read()

