#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import AnalogSensor, UARTDevice
import utime

# Write your program here
ev3 = EV3Brick()
ev3.speaker.beep()

'''
UART SET-UP
'''
sense1 = AnalogSensor(Port.S4, False)
sense1.voltage()
uart = UARTDevice(Port.S4, 9600, timeout = 2000)

def UARTtest():
     uart.write("PLEASE PLEASE WORK.")
     wait(10)
     data = uart.read_all()
     ev3.screen.print(data.decode('utf-8'))
     

'''
MOTOR/SENSOR SET-UP
'''

# # Setup Motors
big_car = Motor(Port.D, Direction.COUNTERCLOCKWISE)
baby_car = Motor(Port.A)

# # Setup Sensors
light_sensor = AnalogSensor(Port.S1, False)
light_sensor.voltage()


# class mySensor(EV3Brick):
#     _ev3dev_driver_name = "ev3-analog-01"
#     def readvalue(self):
#         #self._mode('ANALOG')
#         return self._value(0)

#sens1 = LegoPort(address = 'ev3-ports:in4')
# #sens1.mode = 'ev3-analog'
# utime.sleep(0.5)
# light_sensor = mySensor(Port.S2)

# color_sensor = ColorSensor(Port.S1)
def parseAngle():
    data = uart.read(11)
    data = data.decode('utf-8')
    angle1 = int(data[1,4])
    angle2 = int(data[6,9])
    return angle1, angle2

'''
PROGRAM HERE
'''
# Start code
ev3.speaker.beep()


while True:
    # ......read in joystick controls
    #joy_x_in,joy_y_in = parseAngle()

    #.......print out joystick controls
   #print('x:'+str(joy_x_in))
    #print('y:'+str(joy_y_in))

    #.....drive car
    ##calibrate and scale angles 
        ## if mostly upright, don't move.
        # FOR Y 
        ##-90-10 and 10-90 degrees
        ## -100-20, 20-100 speed

        # FOR X 
        ## max speed +/- 50, min speed +/- 15
        ## -90-10 and 10-90 degrees
    #big_car.run(joy_y_in)
    baby_car.run(15)
        #motor stall??????

    #.....read sensor
    #colorData = color_sensor.color()
    lightData = light_sensor.voltage()
    wait(100)
    #.....send sensor data
    #print('light: '+str(lightData))
    #print('here')

    #UARTtest()
    #uart.write(str(lightData) + ' ')
    #wait(100)
   #data = uart.read()
    #print(data.decode('utf-8'))
    #print(type(data.decode('utf-8')))

    
    
