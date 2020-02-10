#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Write your program here
ev3 = EV3Brick()
ev3.speaker.beep()
rom pybricks.iodevices import AnalogSensor, UARTDevice
# Write your program here
ev3 = EV3Brick()
ev3.speaker.beep()
sense = AnalogSensor(Port.S1, False)
sense.voltage()
uart = UartDevice(Port.S1, 9600, timeout = 2000)


'''
SYSTEMLINK SET-UP
'''
#System Link Interface
import ubinascii, ujson, urequests, utime
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

# # Setup Motors
big_car = Motor(Port.D, Direction.COUNTERCLOCKWISE)
baby_car = Motor(Port.A)

# # Setup Sensors

class mySensor(EV3Brick):
    _ev3dev_driver_name = "ev3-analog-01"
    def readvalue(self):
        #self._mode('ANALOG')
        return self._value(0)

#sens1 = LegoPort(address = 'ev3-ports:in4')
#sens1.mode = 'ev3-analog'
utime.sleep(0.5)
light_sensor = mySensor(Port.S2)

color_sensor = ColorSensor(Port.S1)


'''
PROGRAM HERE
'''
# Start code
ev3.speaker.beep()


while True:
    # ......read in joystick controls
    joy_x_in = 0#float(Get_SL('angleX')) #left right [-90,90]
    joy_y_in = 0#float(Get_SL('angleY')) #forward back [-100,100]
    
    #.......print out joystick controls
    print('x:'+str(joy_x_in))
    print('y:'+str(joy_y_in))

    #.....drive car
    big_car.run(joy_y_in)
    baby_car.run(joy_x_in)

    #.....read sensor
    colorData = color_sensor.color()
    lightData = light_sensor.readvalue()

    #.....send sensor data
    print('light: '+str(lightData))
    print('here')



    
    
