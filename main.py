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

def parseAngle():
    data = uart.read(12)
    wait(10)
    data = data.decode('utf-8')
    angle1 = int(data[1,5])
    angle2 = int(data[7,11])
    return angle1, angle2

def big_car_drive(angle):
    if angle < -10:
        big_car.run(angle - 10)
    elif angle > 10:
        big_car.run(angle + 10)
    wait(10)


def baby_car_drive(angle):
    b = 50
    a = 15
    minAngle = 10
    maxAngle = 90
    speed = ((b-a)*(abs(angle) - minAngle)/(maxAngle-minAngle))+ a
    if angle < -10:
        speed = -speed
    if angle > -10 and angle < 10:
        speed = 0
    baby_car.run(speed)
    wait(10)

def lineDetect(lightdata, whiteLight):
    thresh = 200
    diff = whiteLight - lightdata
    if abs(diff) > 200:
        return 1
    else:
        return 0
    

'''
PROGRAM HERE
'''
# Start code

#calibrate light sensor
wait(1000)
lightData = 0
counter = 0
for i in range(100):
    lightData = light_sensor.voltage() + lightData
    counter = counter + 1
whiteLight = lightData/counter
ev3.speaker.set_volume(150)
ev3.speaker.say("Calibrating Done")
while True:
    # ......read in joystick controls
    #angle1, angle2 = parseAngle()
    angle1, angle2 = 0,0
    #print joystick controlls
    print(angle1, ", ", angle2)
    
    #.....drive car
    baby_car_drive(angle1)
    big_car_drive(angle2)
    
    #.....read sensor
    lightData = light_sensor.voltage()
    wait(100)
    #.....send sensor data
    print('light: ' + str(lightData))
    #print('here')
    isLine = lineDetect(lightData, whiteLight)
    uart.write(str(isLine))
    wait(10)

    
    
