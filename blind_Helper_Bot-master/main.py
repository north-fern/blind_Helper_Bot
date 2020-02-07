#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from pybricks.ev3devio import Ev3devSensor
import utime
import ev3dev2
from ev3dev2.port import LegoPort

'''
SYSTEMLINK SET-UP
'''
#imports API key from separate file
from passwords import Key
     
def SL_setup():
     urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
     headers = {"Accept":"application/json","x-ni-api-key":Key}
     return urlBase, headers
     
def Put_SL(Tag, Type, Value):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     propValue = {"value":{"type":Type,"value":Value}}
     try:
          reply = urequests.put(urlValue,headers=headers,json=propValue).text
     except Exception as e:
          print(e)         
          reply = 'failed'
     return reply

def Get_SL(Tag):
     urlBase, headers = SL_setup()
     urlValue = urlBase + Tag + "/values/current"
     try:
          value = urequests.get(urlValue,headers=headers).text
          data = ujson.loads(value)
          #print(data)
          result = data.get("value").get("value")
     except Exception as e:
          print(e)
          result = 'failed'
     return result
     
def Create_SL(Tag, Type):
     urlBase, headers = SL_setup()
     urlTag = urlBase + Tag
     propName={"type":Type,"path":Tag}
     try:
          urequests.put(urlTag,headers=headers,json=propName).text
     except Exception as e:
          print(e)


'''
MOTOR/SENSOR SET-UP
'''

class mySensor(Ev3devSensor):
    _ev3dev_driver_name = "ev3-analog-01"
    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0)

left_wheel = Motor(Port.A)
right_wheel = Motor(Port.B)
wheelDiam =  56
wheelSpacing = 200

car = DriveBase(left_wheel, right_wheel, wheelDiam, wheelSpacing)

## Setup Sensors
# sens1 = LegoPort(address = 'ev3-ports:in4')
# sens1.mode = 'ev3-analog'
# utime.sleep(0.5)
# sensor_left = mySensor(Port.S2)
# sensor_right = mySensor(Port.S4)


'''
PROGRAM HERE
'''
# Start code
brick.sound.beep()

while True:
     joy_x_in = 50 #left right scaled [-100,100]
     joy_y_in = 50 #forward back [-100,100]

     car.drive(joy_y_in,joy_x_in)



## Take an Input

## drive based on Input

## read sensors

## give sensor data as output
    #1-100
    #average the two sensors?

