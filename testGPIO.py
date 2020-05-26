"""
A GPIO sequence to test hardware

Generally 200 steps per revolution: rn set to 1/2
so 400 steps per revolution
"""

import RPi.GPIO as GPIO
import time

DIRPIN =16 
STEPPIN = 18
STEPSPERREVOLUTION = 800


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DIRPIN, GPIO.OUT)
    GPIO.setup(STEPPIN, GPIO.OUT)


def step(numsteps: int, stepsize: float):
    for i in range(numsteps):
        GPIO.output(STEPPIN, GPIO.HIGH)
        time.sleep(stepsize)
        GPIO.output(STEPPIN, GPIO.LOW)
        time.sleep(stepsize)


def one_revolution_clockwise():
    GPIO.output(DIRPIN, GPIO.HIGH)  # Set direction clockwise
    step(STEPSPERREVOLUTION, .005)


def one_revolution_counterclockwise():
    GPIO.output(DIRPIN, GPIO.LOW)  # Set direction clockwise
    step(STEPSPERREVOLUTION, .005)


if __name__ == '__main__':
    print('Setting up...')
    setup()
    for i in range(5):
        print('One clockwise rotation')
        one_revolution_clockwise()
        print('One counterclockwise rotation')
        one_revolution_clockwise()
        
    print('Finished!')
    GPIO.cleanup()


