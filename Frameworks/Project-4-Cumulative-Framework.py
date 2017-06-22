# Cumulative Arduino Project
# Author: Kip DeCastro
# Created June 16, 2017
# Written for Wyoming EPSCoR Summer Coding Camp 2017
# Version 1.0
# The creation of this code was heavily inspired by and based off of code that
# Matt Cook had designed for the 2016 Summer Coding Camp.

# This is designed to be a cumulative project. I switched the code from the 
# PyMata libraries to pyfirmata because it had less dependencies and seemed easier
# to work from the get-go.
# Got everything looking pretty and working.

# TODO: Fix keyboard interrupt so it actually works. (Not problematic if it 
#       doesn't)

# Import necessary library/ies

import sys
import time
import pyfirmata

from time import sleep

# Define a function to control pin on-off state
def onLED(pin, tf):
    # Write your function here. Hint: use if else statements


    pass
    

# Specify the port for the Arduino.
# For an Arduino Uno on macOS, the port is "/dev/tty.usbmodem1411"
# For an Arduino Uno on Raspbian, the port is "/dev/ttyACM0"

port = "/dev/ttyACM0"

# Define our board so we don't have to type pyfirmata each time.
board = pyfirmata.Arduino(port)

# Starts an iterator so we don't have overflow on Arduino.
# I don't fully understand this, but apparently it is necessary.
it = pyfirmata.util.Iterator(board)
it.start()

# Define our LED numbers. These numbers should correspond to their related 
# digital pin.
# NOTE: Pyfirmata will not allow you to use digital pins 1 and 2

# Set the LED pins for our water level
goodWaterLED = 
badWaterLED = 

# Set the LED pins for our light level
goodLightLED = 
badLightLED = 

# Turn off all the LEDs to begin with
# Hint: We already defined a function that will let us do this...



# Set up the analog pins for our input devices



# This is the main process that our board will loop through.
while True:

    try:
        # Read moisture and light sensor values and store them for testing
        

        # Set the bounds for our values here. These should be experimentally 
        # determined beforehand. 
        """ 
            My values were:
                wetVal (The point at which a plant seems "wet") = 0.8
                lowLight (The highest point I would consider to be dark) = 0.4
                normLight (The highest point for normal indoor light) = 0.6

            This should be a good starting point.
        """          
        wetVal = 
        lowLight = 
        normLight = 

        # The following block checks the moisture level
        # If the moisture level is good, turn on the green light and off the red
        # light   

        if moistureLevel >= wetVal:
            

        # If the moisture level is bad, do the reverse
        elif moistureLevel < wetVal:
            

        # The following block checks the light level
        # If the light is too low, turn on the red light and off the green light
        
        if lightLevel <= lowLight:
            

        # If the light level is at normal indoor light values, turn on both lights
        elif lowLight < lightLevel < normLight:
            

        # If the light level exceeds the normal indoor values, turn on the green
        # and off the red light    
        else :
            

        # wait two seconds before taking our next reading.
        





    except KeyboardInterrupt():
        # Stop communication with the Arduino and Raspberry Pi and turn off the 
        # lights!
        
        board.reset()
        sys.exit()

