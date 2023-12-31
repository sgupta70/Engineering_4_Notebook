#type: ignore 

import board 
import digitalio
import time
import adafruit_mpu6050
import busio

led = digitalio.DigitalInOut(board.GP0) 
led.direction = digitalio.Direction.OUTPUT 
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(board.GP15, board.GP14)
mpu = adafruit_mpu6050.MPU6050(i2c)
print(mpu.acceleration) 

while True:   
    time.sleep(0.5)
    print(f"x angular acceleration: {mpu.acceleration[0]}") # print x value 
    print(f"y angular acceleration: {mpu.acceleration[1]}") # print y value
    print(f"z angular acceleration: {mpu.acceleration[2]}") # print z value 
    print("") # prints a gap 
    time.sleep(1) # wait a second 

    led.value = False # led is off 

    if mpu.acceleration[0] > 9 or mpu.acceleration[0] < -9:
        print("no light") # print that the light is not on 
        led.value = True # led is on if it is tilted to 90 degress
