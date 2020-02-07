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

class mySensor(Ev3devSensor):
    _ev3dev_driver_name = "ev3-analog-01"
    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0)

left = Motor.(A)
right = Motor.(B)
wheelDiam =  56
wheelSpacing = 200

car = DriveBase(left, right, wheelDiam, wheelSpacing)

## Setup Sensors
sens1 = LegoPort(address = 'ev3-ports:in4')
sens1.mode = 'ev3-analog'
utime.sleep(0.5)
sensor_left = mySensor(Port.S2)
sensor_right = mySensor(Port.S4)

# Write your program here

## Take an Input

## drive based on Input

## read sensors

## give sensor data as output
    #1-100
    #average the two sensors?

