#The program will prompt for a location, contact a web service and retrieve JSON for the web service
# and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier
# that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        print('try block')
        js = json.loads(data)
        print('js', js)
    except:
        print('js2', js)
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure to Retrieve ===')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    place = js['results'][0]['place_id']
    print('Place id', place)