"""
A GPIO sequence to test hardware

Generally 200 steps per revolution: rn set to 1/32
so 6400 steps per revolution
"""

import RPi.GPIO as GPIO
import time

DIRPIN = 23
STEPPIN = 24
STEPSPERREVOLUTION = 6400


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DIRPIN, GPIO.OUT)
    GPIO.setup(STEPPIN, GPIO.OUT)

    # Set direction clockwise
    GPIO.output(DIRPIN, 1)


def one_revolution():
    for i in range(STEPSPERREVOLUTION):
        GPIO.output(STEPPIN, 1)
        time.sleep(.001)
        GPIO.output(STEPPIN, 0)
        time.sleep(.001)


if __name__ == '__main__':
    print('Setting up...')
    setup()
    print('Running test code...')
    one_revolution()
    print('Finished!')
    GPIO.cleanup()
