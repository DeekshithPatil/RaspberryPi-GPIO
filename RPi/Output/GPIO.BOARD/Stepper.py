import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

MotorDirection = 16 # GPIO.BOARD pin 16
MotorClock = 18     # GPIO.BOARD pin 18

GPIO.setup(MotorDirection,GPIO.OUT)
GPIO.setup(MotorClock,GPIO.OUT)

def stepperRotate(direction, count):
	if direction == 1:
		GPIO.output(MotorDirection,GPIO.HIGH)
		
		for i in range(count):
			GPIO.output(MotorClock,GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(MotorClock,GPIO.HIGH)
			time.sleep(0.5)
		
	elif direction == 0:
		GPIO.output(MotorDirection,GPIO.LOW)
		
		for i in range(count):
			GPIO.output(MotorClock,GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(MotorClock,GPIO.HIGH)
			time.sleep(0.5)
		
		
	
		
		
