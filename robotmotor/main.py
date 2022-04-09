import RPi.GPIO as GPIO
import time
import sys
from pynput.keyboard import Key, Listener
GPIO.setmode(GPIO.BCM)#GPiomode is BCM
GPIO.setup(4, GPIO.OUT) #Amotorpin out (bcm)
GPIO.setup(17, GPIO.OUT) #Amotorpin out (bcm)
GPIO.setup(9, GPIO.OUT) #Bmotorpin out (bcm)
GPIO.setup(11, GPIO.OUT) #Bmotorpin out (bcm)

def on_press(key):#keyboard find?
    print('{0} pressed'.format(
        key))
    if key == Key.w:
        GPIO.output(4, GPIO.HIGH)

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
