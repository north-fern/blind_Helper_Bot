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
# sense1 = AnalogSensor(Port.S4, False)
# sense1.voltage()
# uart = UARTDevice(Port.S4, 9600, timeout = 2000)

# def UARTtest():
#      uart.write("PLEASE PLEASE WORK.")
#      wait(10)
#      data = uart.read_all()
#      ev3.screen.print(data)
     

'''
MOTOR/SENSOR SET-UP
'''

# # Setup Motors
big_car = Motor(Port.D, Direction.COUNTERCLOCKWISE)
baby_car = Motor(Port.A)

# # Setup Sensors
light_sensor = AnalogSensor(Port.S2, False)
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
    #colorData = color_sensor.color()
    lightData = light_sensor.voltage()

    #.....send sensor data
    print('light: '+str(lightData))
    print('here')

    #UARTtest()



    
    
