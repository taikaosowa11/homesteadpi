#! /usr/bin/python
# General API tutorial: https://www.dataquest.io/blog/python-api-tutorial/
# Weather API: https://openweathermap.org/api/one-call-api

# rain_started webhook for IFTTT (sends notification to phone)
# https://maker.ifttt.com/trigger/rain_started/with/key/omgPi8tG65zRGLig1eXBT7HDc7VEstqyqsRn8Hror6X

# Tai Kao-Sowa
# 4/4/2020
# Test code for Open Weather API Access for the smart homestead project
import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Pull Open Weather API data using API ID
apiid = '464e348ac638930637a5c9e366f2415d' # taikaosowa11@gmail.com account
lat = '37.2796'                            # San Jose Latitude and Longitude
lon = '-121.8947'

check_weather = input('Do you want to update the weather information (yes or no)? ')

if check_weather == 'yes':
    response = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&units=imperial&appid='+apiid)
    print(response.status_code)
    # current, hourly, and daily data
    print('Current weather data')
    jprint(response.json())
else:
    print('Ok, this code does nothing.')

# Regular code goes here
# Eventually, GPIO input would change
