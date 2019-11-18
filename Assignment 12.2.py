#Program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position from the top and follow that link, repeat the process a number of times,
# and report the last name you find.
#http://py4e-data.dr-chuck.net/known_by_Fikret.html
#position 3 (the first name is 1). Follow that link. Repeat this process 4 times.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah

#http://py4e-data.dr-chuck.net/known_by_Rhianna.html

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

def scrapping_web(url):
    print("Retrieving:", url)

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    lst_links = list()
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        x = tag.get('href', None)
        lst_links.append(x)
    return(lst_links)

#Count = 1: Opens URL entered
#Count = 1+1: Scrap and open link at position entered

for i in range(1, count + 2):
    url = scrapping_web(url)[pos-1]
