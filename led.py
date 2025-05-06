from gpiozero import LED
from time import sleep

led = LED(15)  # GPIO22 is pin 15
while True:
	led.on()       # Turn the LED on
sleep(5)       # Keep it on for 5 seconds
led.off()   
