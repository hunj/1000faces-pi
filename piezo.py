import RPi.GPIO as GPIO
import time
import os

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)
    
# pins for the piezo sensor
piezo_1 = 27
piezo_2 = 26

# set the pin modes as input
GPIO.setup(piezo_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(piezo_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val1 = GPIO.input(piezo_1)
        val2 = GPIO.input(piezo_2)
        if val1 > 0:
            print "1"
            os.system('aplay wav/sound1.wav')
        if val2 > 0:
            print "2"
            os.system('aplay wav/sound2.wav')

finally:  
    # Reset the pins back as inputs to prevent frying up upon ctrl-c exit.
    print("Cleaning up")
    GPIO.cleanup()
