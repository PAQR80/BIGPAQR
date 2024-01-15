'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
'''
'''
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1770335.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
count = 0 
tags = soup('span')
for tag in tags:
    print('Contents:', tag.contents[0])
    count = int(tag.contents[0]) + count
print(count)
'''

'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Demi.html'
    
count = 7    
pos = 18

while count > 0:
    # Re-opens the link
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
        
        #Extract 'href=' values
    lst= list()
    tags = soup("a")
    for tag in tags:
        href = tag.get("href", None)
        lst.append(href)
        #prints only the url 'http:/...'
    url = lst[pos-1]
    #prints out the url on that position
    print('Retrieving:', url)
        
    #makes sure the loop isn't infinite
    count = count - 1
'''


'''
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'https://py4e-data.dr-chuck.net/comments_1770337.xml'
print('Retrieving', url)

total = 0
count = 0

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
lst = tree.findall ('comments/comment')

for item in lst:
    count = count + 1
    t = item.find ('count').text
    total = total + float (t)
    
print ('Count:', count)
print ('Sum:' , total)
'''

