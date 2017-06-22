# Light Sensor Project
# Author: Kip DeCastro
# Created June 16, 2017
# Written for Wyoming EPSCoR Summer Coding Camp 2017
# Version 1.0
# The creation of this code was heavily inspired by and based off of code that
# Matt Cook had designed for the 2016 Summer Coding Camp.

# Import necessary library/ies
import sys
from time import sleep

import pyfirmata

# Setup the translator for how we talk to the Arduino
board = pyfirmata.Arduino("/dev/ttyACM0")

it = pyfirmata.util.Iterator(board)
it.start()

# Need to give some time to pyFirmata and Arduino to synchronize
sleep(2)

lightPin = 0

# This is needed to set the Analog pin we are using to report what it observes
analog_0 = board.get_pin('a:0:i')

# This block allows us to quit the program if we want
# by just pressing some keys on the keyboard
while True:
    try:
        # wait a little before reading again.
        # this makes it easier to detect actual differences
        sleep(0.75)
        
        lightLevel = analog_0.read()
        # Print the values so the user can view them
        # print("Light Level: " + str(lightLevel))

        # Optional: Set up ranges of light levels.  Make it print messages for
        # each range. Hint: if we do this we need a way to 
        low = 0.400
        normal = 0.600
        print(lightLevel)
        if lightLevel <= low:
            print("Low light detected")
        elif low < lightLevel < normal:
            print("Moderate light detected")
        else :
            print("Natural light level detected")

# If someone enters something, quit the program and end communcation with the Arduino
    except KeyboardInterrupt() :
        board.close()
        sys.exit()

