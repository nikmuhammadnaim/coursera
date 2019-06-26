from urllib.request import urlopen
from urllib.parse import urlencode
import ssl
import json

# test location = South Federal University
# real location = Georgetown University Law Center

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Service URL
service_url = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = {'address': address, 'key': 42}
    url = service_url + urlencode(parms)
    print('Retrieving', url)


    data = urlopen(url, context=ctx).read().decode()
    print('Retrieved', len(data))

    try:
        js = json.loads(data)
    except:
        js = None
        print('Fail')

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure to Retrieve ===')
        continue

    print(js['results'][0]['place_id'])
