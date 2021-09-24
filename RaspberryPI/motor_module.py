import RPi.GPIO as GPIO
import time

t = 0.01

Motor_R1_Pin = 9
Motor_R2_Pin = 10
Motor_L1_Pin = 27
Motor_L2_Pin = 22
Enable_1 = 17
Enable_2 = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor_R1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_R2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Enable_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Enable_2, GPIO.OUT, initial=GPIO.LOW)

pwm_e1 = GPIO.PWM(Enable_1, 100)
pwm_e2 = GPIO.PWM(Enable_2, 100)
pwm_e1.start(0)
pwm_e2.start(0)

def brake(): # Use reverse rotation to hold the brakes.
   pwm_e1.ChangeDutyCycle(10)
   pwm_e2.ChangeDutyCycle(10)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, True)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, True)
   time.sleep(t)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, False)
   print("Break")

def stop(): # Use Stalled status
   pwm_e1.ChangeDutyCycle(100)
   pwm_e2.ChangeDutyCycle(100)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, False)
   print("Stop")

def forward_1(): # Low speed
   pwm_e1.ChangeDutyCycle(15)
   pwm_e2.ChangeDutyCycle(15)
   GPIO.output(Motor_R1_Pin, True)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, True)
   GPIO.output(Motor_L2_Pin, False)
   print("Forward_Low")
   time.sleep(t)

def forward_2(): # Fast speed
   pwm_e1.ChangeDutyCycle(30)
   pwm_e2.ChangeDutyCycle(30)
   GPIO.output(Motor_R1_Pin, True)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, True)
   GPIO.output(Motor_L2_Pin, False)
   print("Forward_Fast")
   time.sleep(t) 
  
def Reverse(): # Reverse
   pwm_e1.ChangeDutyCycle(15)
   pwm_e2.ChangeDutyCycle(15)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, True)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, True)
   print("Reverse")
   time.sleep(t)

def turnLeft(): # turnLeft
   pwm_e1.ChangeDutyCycle(15)
   pwm_e2.ChangeDutyCycle(20)
   GPIO.output(Motor_R1_Pin, True)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, True)
   print ("Turn_Left")
   time.sleep(t)

def turnLeft_stop(): # turnLeft_stop
   pwm_e1.ChangeDutyCycle(20)
   pwm_e2.ChangeDutyCycle(20)
   GPIO.output(Motor_R1_Pin, True)
   GPIO.output(Motor_R2_Pin, False)
   GPIO.output(Motor_L1_Pin, False)
   GPIO.output(Motor_L2_Pin, True)
   print ("Turn_Left_Stop")
   time.sleep(t)

def turnRight(): # turnRight 
   pwm_e1.ChangeDutyCycle(20)
   pwm_e2.ChangeDutyCycle(15)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, True)
   GPIO.output(Motor_L1_Pin, True)
   GPIO.output(Motor_L2_Pin, False)
   print("Turn_Right")
   time.sleep(t)

def turnRight_stop(): # turnRight_stop 
   pwm_e1.ChangeDutyCycle(20)
   pwm_e2.ChangeDutyCycle(20)
   GPIO.output(Motor_R1_Pin, False)
   GPIO.output(Motor_R2_Pin, True)
   GPIO.output(Motor_L1_Pin, True)
   GPIO.output(Motor_L2_Pin, False)
   print("Turn_Right_Stop")
   time.sleep(t)

#If you want to test the motor, use the script below
'''
while True:
    a = input("")
    a = int(a)
    if a == 1:
       turnRight()
    elif a == 2:
       turnLeft()
   elif a == 3:
       forward_1()
    elif a == 4:
       Reverse()
'''
#GPIO Initialization
def cleanup():
   stop()  
   pwm_e1.stop()
   pwm_e2.stop()
   GPIO.cleanup()
