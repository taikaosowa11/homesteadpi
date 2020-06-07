"""
A basic, basic stepper motor driver class.
This provides really simple functionality to
help us test hardware. It doesn't provide precise
control.
"""

import RPi.GPIO as GPIO
import time
from math import modf

DIRPIN = 16
STEPPIN = 18


class MotorDriver:

    """
    Numsteps = 200 * S1-S2-S3 setting
    For example, if the motor driver is set to ON OFF OFF
    then steps are split into four microsteps, and there
    are 800 steps in one rotation.

    Stepsize determines how quickly the motor interates
    through steps. numsteps*stepsize*2 = seconds/revolution
    """
    def __init__(self, steps_per_rev, step_size):
        self.steps_per_rev = steps_per_rev
        self.step_size = step_size
        self.door_open = False
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(DIRPIN, GPIO.OUT)
        GPIO.setup(STEPPIN, GPIO.OUT)

    def set_door_state(self, state):
        if state == 'open':
            self.door_open = True
        elif state == 'closed':
            self.door_open = False
        else:
            print('Passed an invalid door state!')

    def set_step_size(self, step_size):
        self.step_size = step_size

    def set_steps_per_rev(self, steps_per_rev):
        self.steps_per_rev = steps_per_rev

    def _step(self, revs):
        for i in range(self.steps_per_rev * revs):
            GPIO.output(STEPPIN, GPIO.HIGH)
            time.sleep(self.step_size)
            GPIO.output(STEPPIN, GPIO.LOW)
            time.sleep(self.step_size)

    def revolutions_clockwise(self, revs):
        GPIO.output(DIRPIN, GPIO.HIGH)  # Set direction clockwise
        self._step(revs)
        
    def revolutions_counterclockwise(self, revs):
        GPIO.output(DIRPIN, GPIO.LOW)  # Set direction clockwise
        self._step(revs)

    def open_door(self):
        if not self.door_open:
            self.revolutions_clockwise(3.5)
            self.door_open = True
        else:
            print('Door already open!')

    def close_door(self):
        if self.door_open:
            self.revolutions_counterclockwise(3.5)
            self.door_open = False
        else:
            print('Door already closed!')

    def end(self):
        GPIO.cleanup()
