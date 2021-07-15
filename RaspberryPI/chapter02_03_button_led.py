import RPi.GPIO as GPIO
import time

button_pin=20
led_red,led_orange,led_green = 23,25,12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_orange, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

while 1:
    if GPIO.input(button_pin)==GPIO.HIGH:
        print("PASS!")
        GPIO.output(led_red,0)
        GPIO.output(led_orange,1)
        GPIO.output(led_green,0)
        time.sleep(3)
        GPIO.output(led_red,0)
        GPIO.output(led_orange,0)
        GPIO.output(led_green,1)
        time.sleep(10)        
    else:
        print("Don't CROSS!")
        GPIO.output(led_red,1)
        GPIO.output(led_orange,0)
        GPIO.output(led_green,0)
        time.sleep(0.1)
