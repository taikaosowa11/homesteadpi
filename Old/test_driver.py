"""
A GPIO sequence to test hardware

Generally 200 steps per revolution: rn set to 1/2
so 400 steps per revolution
"""

from driver import MotorDriver

STEPSPERREVOLUTION = 800
STEPSIZE = .001

if __name__ == '__main__':
    driver = MotorDriver(STEPSPERREVOLUTION, STEPSIZE)
    driver.one_revolution_clockwise()
    driver.one_revolution_counterclockwise()
    driver.clockwise_for_time(10)
    driver.counterclockwise_for_time(5)
    driver.end()


