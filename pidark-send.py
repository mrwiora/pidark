import logging
import time
import sys

# from RPi import GPIO
import wiringpi

gpiopin = 0 # this is the wiringpi gpio numeration - in raspberry gpio it would be GPIO17

nextstate = 1
counter = 0
counterrepeat = 0
codestring = ''

wiringpi.wiringPiSetup()
wiringpi.pinMode(gpiopin, 1) # output enable gpiopin

code = sys.argv[1]
codearray = code.split()

while (counterrepeat < 10):
	for i in codearray:
		codestring += str(nextstate)
		if nextstate is 1:
			wiringpi.digitalWrite(gpiopin, 1)
			wiringpi.delayMicroseconds(int(i))
			#time.sleep(int(i) / 1000000)
			nextstate = 0
		else:
			wiringpi.digitalWrite(gpiopin, 0)
			wiringpi.delayMicroseconds(int(i))
			#time.sleep(int(i) / 1000000)
			nextstate = 1
		# print(int(i))
		counter+=1
	print(codestring)
	codestring = ''
	counter = 0
	nextstate = 1
	counterrepeat+=1
