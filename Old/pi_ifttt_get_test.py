#! /usr/bin/python

import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# The button set up with IFTTT will tell this address "close"
response = requests.get('https://maker.ifttt.com/trigger/coop/with/key/omgPi8tG65zRGLig1eXBT7HDc7VEstqyqsRn8Hror6X')
print(response.status_code)
# current, hourly, and daily data
print('Info received from IFTTT')
print(response.text)
