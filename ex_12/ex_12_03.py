# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Data Collection
URL = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


print('Retrieving: %s' % URL)
for i in range(0, count):
    html = urllib.request.urlopen(URL, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    cnt = 0
    pst = 0
    for tag in tags:
        pst += 1
        if pst == position:
            print('Retrieving: %s' % str(tag.get('href', None)))
            URL = str(tag.get('href', None))
            ps = 0
            break
