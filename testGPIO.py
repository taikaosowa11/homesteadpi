"""
A GPIO sequence to test hardware

Generally 200 steps per revolution: rn set to 1/2
so 400 steps per revolution
"""

import RPi.GPIO as GPIO
import time

DIRPIN =16 
STEPPIN = 18
STEPSPERREVOLUTION = 400 # test


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DIRPIN, GPIO.OUT)
    GPIO.setup(STEPPIN, GPIO.OUT)

def one_revolution_clockwise():

    # Set direction clockwise
    GPIO.output(DIRPIN, GPIO.HIGH)
    
    for i in range(STEPSPERREVOLUTION):
        GPIO.output(STEPPIN, GPIO.HIGH)
        time.sleep(.01)
        GPIO.output(STEPPIN, GPIO.LOW)
        time.sleep(.01)


if __name__ == '__main__':
    print('Setting up...')
    setup()
    print('Running test code...')
    one_revolution()
    print('Finished!')
    GPIO.cleanup()


