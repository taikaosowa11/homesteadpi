#!/usr/bin/env python3

import RPi.GPIO as GPIO
import requests 

def button_callback(channel):
  r = requests.post('https://maker.ifttt.com/trigger/rain_started/with/key/omgPi8tG65zRGLig1eXBT7HDc7VEstqyqsRn8Hror6X', params={"value1":"none","value2":"none","value3":"none"})
  print('Button pressed, IFTTT notification sent')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# use gpio pin 10, activate built in pull down resistor
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback, bouncetime = 200)
message = input('Press enter to quit\n')

#while True:
#  state = GPIO.input(10)
#  if state == True:
#    print('Button Pressed')
#    time.sleep(1)

GPIO.cleanup()
