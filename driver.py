"""
A basic, basic stepper motor driver class.
This provides really simple functionality to
help us test hardware. It doesn't provide precise
control.
"""

import RPi.GPIO as GPIO
import time

"""
Numsteps = 200 * S1-S2-S3 setting
For example, if the motor driver is set to ON OFF OFF
then steps are split into four microsteps, and there
are 800 steps in one rotation.

Stepsize determines how quickly the motor interates
through steps. numsteps*stepsize*2 = seconds/revolution
"""

steps_per_rev = 800
step_size = .001
door_open = True
DIRPIN = 16
STEPPIN = 18

def set_door_state(state):
    global door_open
    if state == 'open':
        door_open = True
    elif state == 'closed':
        door_open = False
    else:
        print('Passed an invalid door state!')


def set_step_size(s):
    global step_size
    step_size = s


def set_steps_per_rev(s):
    global steps_per_rev
    steps_per_rev = s


def _step(revs):
    for i in range(int(steps_per_rev * revs)):
        GPIO.output(STEPPIN, GPIO.HIGH)
        time.sleep(step_size)
        GPIO.output(STEPPIN, GPIO.LOW)
        time.sleep(step_size)


def revolutions_clockwise(revs):
    GPIO.output(DIRPIN, GPIO.HIGH)  # Set direction clockwise
    _step(revs)


def revolutions_counterclockwise(revs):
    GPIO.output(DIRPIN, GPIO.LOW)  # Set direction clockwise
    _step(revs)


def open_door():
    print('Opening door...')
    global door_open
    if not door_open:
        revolutions_clockwise(3.5)
        door_open = True
    else:
        print('Door already open!')


def close_door():
    print('Closing door...')
    global door_open
    if door_open:
        revolutions_counterclockwise(3.5)
        door_open = False
    else:
        print('Door already closed!')


def end():
    GPIO.cleanup()
