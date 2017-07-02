#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv
# http://RasPi.tv/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3
import RPi.GPIO as GPIO
import subprocess
GPIO.setmode(GPIO.BCM)

# GPIO 17 & 27 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# GPIO 26 set up as an input, pulled down, connected to 3V3 on button press
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# GPIO 16 set up as output for LED
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.LOW)

# now we'll define two threaded callback functions
# these will run in another thread when our events are detected
def my_callback(channel):
    print "falling edge detected on 27"

def my_callback2(channel):
    print "falling edge detected on 17"
    GPIO.output(16, GPIO.HIGH)
    subprocess.Popen("sudo node server.js ForceChange", cwd='/home/mumble/raspberry-wifi-conf', shell=True)
    GPIO.output(16, GPIO.LOW)

print "Make sure you have a button connected so that when pressed"
print "it will connect GPIO port 17 (pin 11) to GND (pin 6)\n"
print "You will also need a second button connected so that when pressed"
print "it will connect GPIO port 26 (pin 37) to 3V3 (pin 1)\n"
print "You will also need a third button connected so that when pressed"
print "it will connect GPIO port 27 (pin 13) to GND (pin 14)"

# when a falling edge is detected on port 27, regardless of whatever
# else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(27, GPIO.FALLING, callback=my_callback, bouncetime=300)

# when a falling edge is detected on port 17, regardless of whatever
# else is happening in the program, the function my_callback2 will be run
# 'bouncetime=300' includes the bounce control written into interrupts2a.py
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback2, bouncetime=300)

try:
    print "Waiting for rising edge on port 26"
    GPIO.wait_for_edge(26, GPIO.RISING)
    print "Rising edge detected on port 26. Here endeth the third lesson."

except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
