#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract
# the comment counts from the JSON data, compute the sum of the numbers in the file

import urllib.request, urllib.parse, urllib.error
import ssl
import json

addsum = 0
x = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
    js = js["comments"]
except:
    js = None

#print(json.dumps(js, indent=4))

for item in js:
    x = x + 1
    addsum += int(item["count"])

print("Count:", x)
print("Sum:", addsum)
