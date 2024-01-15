'''
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1770338.json'
print('Retrieving', url)

total = 0
count = 0

uh = urllib.request.urlopen(url)
data = uh.read().decode()
try : 
    js=json.loads(data)
except:
    js=None

print(json.dumps(js,indent=4))

for u in js['comments']:
    total = total + u['count']

print (total)
'''
import re

hand = open("regex_sum_24962.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)