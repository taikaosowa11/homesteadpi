#! /usr/bin/python
"""
Code: schedule_door.py
Description: Basic code that actuates chicken coop door at sunrise/sunset
for the homestead pi project. Accesses the Open Weather API.

Author: Tai Kao-Sowa
Date: 6/6/20
"""
import requests
from datetime import datetime
import pytz
import schedule
import time


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

    # Switch to local timezone
    sunrise = sunrise.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("America/Los_Angeles"))
    sunset = sunset.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("America/Los_Angeles"))
    return sunrise, sunset
