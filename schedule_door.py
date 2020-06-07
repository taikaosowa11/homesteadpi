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
from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from apscheduler.schedulers.background import BackgroundScheduler
import driver as dr
import pytz
import time

open_time = ''
close_time = ''


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
    global open_time
    global close_time
    open_time = sunrise.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("America/Los_Angeles")).strftime("%H:%M:%S")
    close_time = post_sunset.replace(tzinfo=pytz.utc).astimezone(pytz.timezone("America/Los_Angeles")).strftime("%H:%M:%S")


def listener(event):
    if not event.exception:
        job = scheduler.get_job(event.job_id)
        if job.name and job.name == 'get_sunrise_sunset':
            scheduler.add_job(dr.open_door, 'date', open_time, misfire_grace_time=2, coalesce=True)
            scheduler.add_job(dr.close_door, 'date', close_time, misfire_grace_time=2, coalesce=True)


if __name__ == '__main__':
    print('Starting!')
    scheduler = BackgroundScheduler()
    scheduler.add_listener(listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    # at 3 am every day, get sunrise and sunset
    # make sure to run this code on boot as well
    scheduler.add_job(get_sunrise_sunset, 'cron', hour='3', misfire_grace_time=2, coalesce=True)
    scheduler.start()

    try: # Also, wait for button press!
        while True:
            time.sleep(.5)

    except (KeyboardInterrupt, SystemExit):
        print('Scheduler shutting down')
        scheduler.shutdown()

"""

    # GPIO setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    pinpir = 17
    GPIO.setup(pinpir, GPIO.IN)
    currentstate = 0
    previousstate = 0
"""