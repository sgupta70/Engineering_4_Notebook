# type: ignore
import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import pwmio 
from adafruit_motor import servo

ledRed = digitalio.DigitalInOut(board.GP18)
ledRed.direction = digitalio.Direction.OUTPUT
ledGreen = digitalio.DigitalInOut(board.GP13)
ledGreen.direction = digitalio.Direction.OUTPUT # red and green led output location

btn = DigitalInOut(board.GP15)
btn.direction = Direction.INPUT
btn.pull = Pull.UP # set pin number and input as pull up

prev_state = btn.value # new variable

pwm = pwmio.PWMOut(board.GP14, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

while True:
    cur_state = btn.value # new variable
    if cur_state != prev_state: # if the state of the button changes
        if not cur_state: # if the button is pressed
            print("Button pushed")
            for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
                print(x) # print the variable
                ledRed.value = True
                time.sleep(0.5)
                ledRed.value = False
                time.sleep(0.5) # blink red led
            ledGreen.value = True 
            print("Launch")
            for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
                my_servo.angle = angle
                time.sleep(0.05)
            time.sleep(3.0)
            ledGreen.value = False # turn on green light and print launch then turn the light off after 3 seconds
            for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
                my_servo.angle = angle
            time.sleep(0.05)
        else:
            print("Button is up")

    prev_state = cur_state # reset button value to unpressed