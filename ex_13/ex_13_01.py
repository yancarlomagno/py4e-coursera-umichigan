import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Run program as long as addresses are inputted
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

# Retrieve address and number of characters
    adress = input('Enter location: ')
    html = urllib.request.urlopen(address).read().decode()
    print('Retrieving', address)
    print('Retrieved', len(html), 'characters')

#data calculation
    count = 0
    sum = 0

    data = ET.fromstring(html)
    tags = data.findall('comments/comment')

    for tag in tags:
        count += 1
        sum += int(tag.find('count').text)

    print('Count:', count)
    print('Sum:', sum)
