#type: ignore 
import time
import board
import digitalio

ledRed = digitalio.DigitalInOut(board.GP18)
ledRed.direction = digitalio.Direction.OUTPUT
ledGreen = digitalio.DigitalInOut(board.GP13)
ledGreen.direction = digitalio.Direction.OUTPUT # red and green led output location

for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
    print(x) # print the variable
    ledRed.value = True
    time.sleep(0.5)
    ledRed.value = False
    time.sleep(0.5) # blink red led
print("Launch")
ledGreen.value = True
time.sleep(5.0) # green led on for 5 secs