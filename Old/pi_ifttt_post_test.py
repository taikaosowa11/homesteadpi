#! /usr/bin/python

# Imports
import RPi.GPIO as GPIO
import time
import requests

# The main important line. The rest is GPIO copied from web for reference
r = requests.post('https://maker.ifttt.com/trigger/rain_started/with/key/omgPi8tG65zRGLig1eXBT7HDc7VEstqyqsRn8Hror6X', params={"value1":"none","value2":"none","value3":"none"})

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)

# Turn off GPIO warnings
GPIO.setwarnings(False)

# Set a variable to hold the GPIO Pin identity
# This could be a motion sensor in the chicken coop
pinpir = 17

# Set GPIO pin as input
GPIO.setup(pinpir, GPIO.IN)

# Variables to hold the current and last states
currentstate = 0
previousstate = 0

try:
    print("Waiting for PIR to settle ...")

    # Loop until PIR output is 0
    while GPIO.input(pinpir) == 1:

        currentstate = 0

    print(" Ready")

    # Loop until users quits with CTRL-C
    while True:

        # Alternatively, use API data here. No code yet
        # Read PIR state
        currentstate = GPIO.input(pinpir)

        # If the PIR is triggered
        if currentstate == 1 and previousstate == 0:

            print("Rain has started!")

            # Your IFTTT URL with event name, key and json parameters (values)
            r = requests.post('https://maker.ifttt.com/trigger/rain_started/with/key/omgPi8tG65zRGLig1eXBT7HDc7VEstqyqsRn8Hror6X', params={"value1":"none","value2":"none","value3":"none"})

            # Record new previous state
            previousstate = 1

            #Wait 120 seconds before looping again
            print("Waiting 120 seconds")
            time.sleep(120)

        # If the PIR has returned to ready state
        elif currentstate == 0 and previousstate == 1:

            print("Ready")
            previousstate = 0

        # Wait for 10 milliseconds
        time.sleep(0.01)

except KeyboardInterrupt:
    print(" Quit")

    # Reset GPIO settings
    GPIO.cleanup()
