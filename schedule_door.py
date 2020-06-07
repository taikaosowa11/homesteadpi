#! /usr/bin/python
"""
Code: schedule_door.py
Description: Basic code that actuates chicken coop door at sunrise/sunset
for the homestead pi project. Accesses the Open Weather API.

Author: Tai Kao-Sowa
Date: 6/6/20
"""
import requests
from datetime import datetime, timedelta
import pytz
import os

def get_sunrise_sunset():
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
    sunrise = datetime.utcfromtimestamp(data['current']['sunrise'])
    sunset = datetime.utcfromtimestamp(data['current']['sunset'])

    # add 15 minutes to make sure the chickens are in the coop!
    post_sunset = sunset + timedelta(minutes=15)

    # Switch to local timezone
    sunrise = sunrise.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("America/Los_Angeles"))
    post_sunset = post_sunset.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("America/Los_Angeles"))
    return sunrise, post_sunset


if __name__ == '__main__':

    open_time, close_time = get_sunrise_sunset()
    sched_open = 'echo python3 /home/pi/homesteadpi/actuate_door.py open | at ' + open_time.strftime('%H:%M')
    sched_close = 'echo python3 /home/pi/homesteadpi/actuate_door.py close | at ' + close_time.strftime('%H:%M')
    os.system(sched_open)
    os.system(sched_close)

    import time
    while True:
        print('Waiting to press button...')
        time.sleep(30)
