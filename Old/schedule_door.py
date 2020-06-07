#! /usr/bin/python
# General API tutorial: https://www.dataquest.io/blog/python-api-tutorial/
# Weather API: https://openweathermap.org/api/one-call-api

# rain_started webhook for IFTTT (sends notification to phone)
# https://maker.ifttt.com/trigger/rain_started/with/key/omgPi8tG65zRGLig1eXBT7HDc7VEstqyqsRn8Hror6X

# Tai Kao-Sowa
# 4/4/2020
# Test code for Open Weather API Access for the smart homestead project
import requests
from datetime import datetime
import pytz
import schedule
import time

# Get Open Weather API data
apiid = '464e348ac638930637a5c9e366f2415d'  # taikaosowa11@gmail.com account
lat = '37.2796'  # San Jose Latitude and Longitude
lon = '-121.8947'

# Use imperial units
response = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='
                        + lat + '&lon=' + lon + '&units=imperial&appid=' + apiid)

# current, minutely, hourly, daily data
# Right now we just get sunrise and sunset
data = response.json()
sunrise = data['current']['sunrise']
sunset = data['current']['sunset']
sunrise = datetime.utcfromtimestamp(sunrise)
sunset = datetime.utcfromtimestamp(sunset)

# Switch to local timezone
sunrise = sunrise.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("America/Los_Angeles"))
sunset = sunset.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("America/Los_Angeles"))

print('Sunrise: ', sunrise.strftime('%c'))
print('Sunset: ', sunset.strftime('%c'))
