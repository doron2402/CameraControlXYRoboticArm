import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor1A = 15
Motor1B = 18
Motor1E = 23

Motor2A = 9
Motor2B = 11
Motor2E = 5
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)


GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

print "Turning motor1 on"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(20)
 
print "Stopping motor1"
GPIO.output(Motor1E,GPIO.LOW)

sleep(5)
print "Turning motor2 on"
GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)

sleep(20)
 
print "Stopping motor2"
GPIO.output(Motor2E,GPIO.LOW)

sleep(5)
print "Turning motor1 and motor2 on"
GPIO.output(Motor1E,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)

sleep(10)
print "Stopping motor1 and motor2 on"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
 
GPIO.cleanup()