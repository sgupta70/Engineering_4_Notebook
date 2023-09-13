#type: ignore 
import time
import board
import digitalio

ledRed = digitalio.DigitalInOut(board.GP18)
ledRed.direction = digitalio.Direction.OUTPUT
ledGreen = digitalio.DigitalInOut(board.GP13)
ledGreen.direction = digitalio.Direction.OUTPUT # red and green led output location

btn = digitalio.DIgitalInOut(board.GP15)
btn.direction = Direction.INPUT 
btn.pull = Pull.Up

prev_state = btn.value 

while True
    cur_state = btn.value 
    if cur_state != prev_state:
        if not cur_state:
    for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
       print(x) # print the variable
     ledRed.value = True # turn red led on 
     time.sleep(0.5)
     ledRed.value = False # turn red led off 
     time.sleep(0.5) # blink red led
    print("Launch")
    ledGreen.value = True #turn green led on 
    time.sleep(5.0) # green led on for 5 sec