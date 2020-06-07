from driver import MotorDriver
import sys

STEPSPERREVOLUTION = 800
STEPSIZE = .001

if sys.argv[1] == 'open':
    print('Opening door...')
    driver = MotorDriver(STEPSPERREVOLUTION, STEPSIZE)
    driver.motor_open_door()
elif sys.argv[1] == 'close':
    print('Closing door...')
    driver = MotorDriver(STEPSPERREVOLUTION, STEPSIZE)
    driver.motor_close_door()
else:
    print('Invalid command to actuate_door.py!')

