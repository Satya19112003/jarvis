import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED = 18
GPIO.setup(LED, GPIO.OUT)

def lights_on():
    GPIO.output(LED, GPIO.HIGH)

def lights_off():
    GPIO.output(LED, GPIO.LOW)

if __name__ == "__main__":
    lights_on()
    time.sleep(5)
    lights_off()

