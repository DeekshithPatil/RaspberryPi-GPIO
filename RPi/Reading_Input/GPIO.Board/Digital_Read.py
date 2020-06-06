import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

inputpin = 7

GPIO.setup(inputpin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	value = GPIO.input(inputpin)
	print ("Value = ", value)
