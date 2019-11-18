#Scraping Numbers from HTML using BeautifulSoup
#Read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
# http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_266670.html >>>> Sum: 2575

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

sum = 0
lst = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Connect to URL and read data
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read() #Read whoe data at once
soup = BeautifulSoup(html, 'html.parser')
tags = soup('tr')

for tag in tags:
    # Look at the parts of a tag
    print('tag: ', tag)
    lines = tag.contents[1]
    for line in lines:
        # Regex to extract only numbers and convert to string
        num = re.findall('[0-9]+', str(line))
        lst.extend(num)

# Calculate sum of each elements in list
for x in lst:
    sum += int(x)

print(sum)