import RPi.GPIO as GPIO
import time
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.IN)

print('Starting')

while True: 

    if (GPIO.input(5) == GPIO.HIGH):
        GPIO.output(4, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(4, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)

        subprocess.run(['aplay', 'Front_Left.wav'])
    else: 
        GPIO.output(4, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)

print('Done')

