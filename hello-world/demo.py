#!/usr/bin/env python3
from ev3dev.ev3 import *
import os

#Change the size of the text that will be printed on the EV3 Screen
os.system('setfont Lat15-TerminusBold14')

#Print a message to the screen, and make the EV3 Speak
print('Hello, my name is EV3!')
Sound.speak('Hello, my name is EV3').wait()