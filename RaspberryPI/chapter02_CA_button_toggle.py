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

light_on=False
def button_callback(channel):
    global light_on
    if light_on==False:
        GPIO.output(led_red,0)
        GPIO.output(led_orange,0)
        GPIO.output(led_green,0)
        print("LED OFF!")
    else:
        GPIO.output(led_red,1)
        GPIO.output(led_orange,1)
        GPIO.output(led_green,1)
        print("LED ON!")
    light_on=not light_on

GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_callback, bouncetime=300)

while 1:
    time.sleep(0,1)
