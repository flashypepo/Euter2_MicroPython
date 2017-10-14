""" demo of Ultrasonic device with ultrasonic module of Euter2.
2017-1014 PePo adopted for MicropPython 1.9+, configuration ESP32 / Wemos Lolin32 (Revision 0)
"""
import ultrasonic
from time import sleep

# GPIO pins for specific development board Wemos D1 mini
# PePo: not relevant for WeMOS Lolin32
#gpio = {"TX":01, "RX":03, "D0": 16, "D1": 05, "D2": 04, "D3": 00, "D4": 02, "D5": 14, "D6": 12, "D7": 13, "D8": 15}

trigger = 12 #gpio[ "D6" ]
echo = 14 #gpio[ "D5" ]

#create sensor hc on pins trigger and echo
hc = ultrasonic.Ultrasonic( trigger, echo)

dist = 0  # distance value

while True:
    # Get reading from sensor
    ''' distance in meters
    dist = hc.distance()
    print('afstand is {0:4.1f} m'.format(dist))
    #'''
    #''' distance in cm
    dist = hc.distance_in_cm()
    print('afstand is {0:3.1f} m'.format(dist))
    #'''
    sleep(1)

