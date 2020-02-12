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

'''
FUNCTIONS
'''

def UARTtest():
    '''
    a test function for debugging UART
    '''
    uart.write("PLEASE PLEASE WORK.")
    wait(10)
    data = uart.read_all()
    ev3.screen.print(data.decode('utf-8'))
     

def parseAngle():
    '''
    attempts to read in data from the buffer and parse it
    data in format b'(XXXXX,XXXXX)'
    '''
    uart.clear()
    angle1 = 0
    angle2 = 0
    try:
        data = uart.read(13)
        wait(10)
        data = data.decode('utf-8')
        print("data type: ", type(data))
        print("data: ", data)
        angle1 = int(data[1:6])
        angle2 = int(data[7:12])
    except:
        print("FAILED READ FROM CONTROLLER")
    return angle1, angle2

def big_car_drive(angle):
    '''
    Drives the Big car given an Angle
    '''
    b = 40
    a = 15
    minAngle = 15
    maxAngle = 90
    speed = ((b-a)*(abs(angle) - minAngle)/(maxAngle-minAngle))+ a
    if angle < -minAngle:
        speed = -speed
    if angle > -minAngle and angle < minAngle:
        speed = 0
    big_car.run(speed)
    wait(10)

def baby_car_drive(angle):
    '''
    Drives the baby car given an Angle
    '''
    b = 40
    a = 15
    minAngle = 15
    maxAngle = 90
    speed = ((b-a)*(abs(angle) - minAngle)/(maxAngle-minAngle))+ a
    if angle < -minAngle:
        speed = -speed
    if angle > -minAngle and angle < minAngle:
        speed = 0
    baby_car.run(speed)
    wait(10)

def lineDetect(lightdata, whiteLight):
    '''
    detects the line and either returns 1 or 0
    '''
    thresh = 300
    diff = whiteLight - lightdata
    if abs(diff) > thresh:
        return 1
    else:
        return 0
    
def lightCalibration():
    '''
    calibrates the light sensor on the background
    '''
    wait(1000)
    lightData = 0
    counter = 0
    for i in range(100):
        lightData = light_sensor.voltage() + lightData
        counter = counter + 1
    whiteLight = lightData/counter
    return whiteLight
'''
PROGRAM HERE
'''
ev3.speaker.beep()
'''
UART SET-UP
'''
sense1 = AnalogSensor(Port.S4, False)
sense1.voltage()
uart = UARTDevice(Port.S4, 9600, timeout = 2000)

'''
MOTOR/SENSOR SET-UP
'''

# # Setup Motors
big_car = Motor(Port.D, Direction.COUNTERCLOCKWISE)
baby_car = Motor(Port.A)

# # Setup Sensors
light_sensor = AnalogSensor(Port.S1, False)
light_sensor.voltage()

#calibrate light sensor
whiteLight = lightCalibration()
ev3.speaker.set_volume(100)
ev3.speaker.say("Calibration Complete")

while True:
    # ......read in joystick controls
    angle1, angle2 = parseAngle()

    #print joystick controlls
    print("ANGLES: ", angle1, ", ", angle2)

    #.....drive car
    baby_car_drive(angle1)
    big_car_drive(angle2)
    
    #.....read sensor
    lightData = light_sensor.voltage()
    #wait(10)
    #.....send sensor data
    print('light: ' + str(lightData))
    isLine = lineDetect(lightData, whiteLight)
    uart.write(str(isLine))
    print('isLine: ' + str(isLine))
    #wait(10)