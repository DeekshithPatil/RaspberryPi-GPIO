import RPi.GPIO as GPIO
import atexit
import time

def exit_handler():
    GPIO.cleanup() #Cleanup GPIO functions after exit

atexit.register(exit_handler) #execute exit_handler() when execution is terminated

def my_callback(channel):
    print("The switch changed")

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(7,GPIO.RISING,callback=my_callback)

while True:
    # here's where your code does something while it waits
    time.sleep(3)
    print("waiting...")
    


