# Moisture Sensor Project
# Author: Kip DeCastro
# Created June 16, 2017
# Written for Wyoming EPSCoR Summer Coding Camp 2017
# Version 1.0
# The creation of this code was heavily inspired by and based off of code that
# Matt Cook had designed for the 2016 Summer Coding Camp.

# Import libraries to interact with Arduino
import sys
import time
import pyfirmata

# Setup the translator for how we talk to the Arduino
board = pyfirmata.Arduino("/dev/ttyACM0")

it = pyfirmata.util.Iterator(board)
it.start()

# Set what "wet" is and store that in a variable
wetVal = 0.8   # CHANGE ME

# Set which pin(s) we will use to monitor moisture levels
moisturePin = 0

# Make the analog pin 0 tell us what it is observing
analog_0 = board.get_pin('a:0:i')

# Loop through this process
while True:
    # Wait a little so we can see the values a little more clearly.  This way we can see what is happening more easily.
    time.sleep(0.75)

    try:
        # Read moisture sensor values and store it for testing
        moistureLevel = analog_0.read()

        # Test if sensor is wet
        if moistureLevel >= wetVal:
            # Show the user the sensor is wet and how wet it is
            print("The sensor is wet! \nThe moisture level is: " + str(moistureLevel))
        # If the sensor is not wet, print an error.
        else :
            # Show the user that the sensor is not wet
            print("The sensor is dry! \nThe moisture level is: " + str(moistureLevel))
    except KeyboardInterrupt():
        # Stop communication with the Arduino and Raspberry Pi
        board.reset()
        sys.exit()

