"""
A basic, basic stepper motor driver class.
This provides really simple functionality to
help us test hardware. It doesn't provide precise
control.
"""

import RPi.GPIO as GPIO
import time

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
    def __init__(self, steps_per_rev: int, step_size: float):
        self.steps_per_rev = steps_per_rev
        self.step_size = step_size
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(DIRPIN, GPIO.OUT)
        GPIO.setup(STEPPIN, GPIO.OUT)

    def set_step_size(self, step_size: int):
        self.step_size = step_size

    def set_steps_per_rev(self, steps_per_rev: int):
        self.steps_per_rev = steps_per_rev

    def one_revolution_clockwise(self):
        GPIO.output(DIRPIN, GPIO.HIGH)  # Set direction clockwise
        self._step(self.steps_per_rev, self.step_size)

    def one_revolution_counterclockwise(self):
        GPIO.output(DIRPIN, GPIO.LOW)  # Set direction clockwise
        self._step(self.steps_per_rev, self.step_size)

    """
    This is a bit ugly, but since we're using this as a pulley
    it works for now. We might want to actually use the stepper
    motor for sub-unit rotations in the future, and then this
    will have to change.
    """
    def clockwise_for_time(self, dur: int):
        sec_per_rev = self.numsteps*self.stepsize*2
        num_revs = round(dur/sec_per_rev)
        for i in range(num_revs):
            self.one_revolution_clockwise()

    def counterclockwise_for_time(self, dur: int):
        sec_per_rev = self.numsteps*self.stepsize*2
        num_revs = round(dur/sec_per_rev)
        for i in range(num_revs):
            self.one_revolution_counterclockwise()

    def _step(self):
        for i in range(self.numsteps):
            GPIO.output(STEPPIN, GPIO.HIGH)
            time.sleep(self.stepsize)
            GPIO.output(STEPPIN, GPIO.LOW)
            time.sleep(self.stepsize)

    def end(self):
        GPIO.cleanup()
