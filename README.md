# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)
* [LED_Blink](#led_blink)
* [Launch_Pad_Assignment](#launch_pad_assignment)
* [Crash_Avoidance_Assignment](#crash_avoidance_assignment)



&nbsp;

## Raspberry_Pi_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Hyper Link Text](https://github.com/sgupta70/Engineering_4_Notebook/tree/main/raspberry-pi)

### Test Image
![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/76e5353f-ab72-4726-9d29-1d0888f9fb80)

### Test GIF
![602ab530c815e image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/815288c0-5e51-45d7-a89e-f978ec7a1821)



## LED_Blink

### Assignment Description

For this assignment we had to set up our VS Code so it would be connected to GitHub and get a Raspberry Pi Pico to blink.

### Evidence 

![ezgif com-crop](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/0ac23d86-3241-46a1-bcbd-60724e039f2f)


### Wiring

No wiring, plugged right into the computer 

### Code
```
import board 
import digitalio 
import time 

led = digitalio.DigitalInOut(board.LED) 
led.direction = digitalio.Direction.OUTPUT 

while True: 
    led.value = True 
    time.sleep(0.5)
    led.value = False 
    time.sleep(0.5)
  ```
 [Code](https://github.com/sgupta70/Engineering_4_Notebook/blob/main/LED_blink.py)
 
### Reflection

A majority of this assignment was getting our computers set up and connecting VS Code with Github. The code part was very simple, there was no wiring needed so the pico was plugged right into the computer. The code would just turn the LED on and off. It was super simple and a good way to get back into coding for the new year. 

## Launch_Pad_Assignment

## Part 1 

### Assignment Description

For this assignment we had to get our serial monitor to print a countdown which was counting down from 10

### Evidence 

![ezgif com-optimize (1)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/91e85500-1036-4b44-96cc-9e324c315a18)

### Wiring

No wiring, plugged right into the computer 

### Code
```
import board 
import digitalio 
import time 

while True: 
    for x in range(10, -1, -1): # in the range from 10 to 0 going down by 1
        time.sleep(1) # wait a second 
        print(x)  # print the variable
    print ("Launch") 
    time.sleep(2) # wait 2 seconds
    
  ```
 
### Reflection

This assignment wasn't very hard, I used the range() function  

## Part 2

### Assignment Description

For this part we had to get two LEDs to blink with the countdown, flashing red as it counts down from ten and then turns green when it prints "launch". 

### Evidence 

![ezgif com-resize](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/8bf5a4a4-6273-4a8b-92cc-04161d98ef88)


### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/9273f53b-699c-46c2-ab94-15fcf7f62ce8)


### Code
```
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
    
  ```
 
### Reflection

This assignment wasn't super hard using the code I had from part 1 I just added on to turn on the red and green LED. 

## Part 3

### Assignment Description

For this part we had to press a button which would then get two LEDs to blink with the countdown, flashing red as it counts down from ten and then turns green when it prints "launch". 

### Evidence 

![ezgif com-optimize](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/384cad2e-5eac-4729-a733-671b42b083fc)


### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/1d8b4772-412d-4ca4-b1e0-0f1792f9279d) 

### Code
```
# type: ignore
import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull

ledRed = digitalio.DigitalInOut(board.GP18)
ledRed.direction = digitalio.Direction.OUTPUT
ledGreen = digitalio.DigitalInOut(board.GP13)
ledGreen.direction = digitalio.Direction.OUTPUT # red and green led output location

btn = DigitalInOut(board.GP15)
btn.direction = Direction.INPUT
btn.pull = Pull.UP # set pin number and input as pull up

prev_state = btn.value # new variable

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
            time.sleep(3.0)
            ledGreen.value = False # turn on green light and print launch then turn the light off after 3 seconds
        else:
            print("Button is up")

    prev_state = cur_state # reset button value to unpressed
  ```
 
### Reflection

This assignment wasn't super hard using my knowledge from last year I knew how to get a button to work. I just put the code for the button into my existing code from part 2. In the beginning the code wouldn't load onto the pico but I figured it out and realized it wasn't uploading to the D drive so once I fixed that it worked. 

## Part 4

### Assignment Description

For this part we had to press a button which would then get two LEDs to blink with the countdown, flashing red as it counts down from ten and then turns green and moves the servo when it "launches". 

### Evidence 

![ezgif com-optimize (3)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/d730d765-c9b4-47cd-9032-c1acf9051cdc)


### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/82896b62-b3e1-4695-90cc-4005b2729d48)

### Code
```
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
  ```
 
### Reflection

This was the final part for this assignment, I used to code that I already had and added in code for a servo which I remembered from last year. It wasn't working and we realized that one of my wires wasn't going into the correct pin so after switching that it all worked together. This assignment was a good way to get into code. 


## Crash_Avoidance_Assignment

## Part 1 

### Assignment Description

For this assignment we had to wire up an accelerometer and get it to print out the x, y, and z values on the serial monitor. 

### Evidence 

![ezgif com-crop (3)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/8844d422-a745-4fed-9fba-417db9241eea)

### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/f3594102-ce2c-4bd0-8c28-24206cadcea1)

### Code
```
#type: ignore 

import board 
import digitalio
import time
import adafruit_mpu6050
import busio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(board.GP15, board.GP14)
mpu = adafruit_mpu6050.MPU6050(i2c)
print(mpu.acceleration) 

while True:   
    print(f"x angular velocity: {mpu.gyro[0]}") # print x value 
    print(f"y angular velocity: {mpu.gyro[1]}") # print y value
    print(f"z angular velocity: {mpu.gyro[2]}") # print z value 
    print("") # prints a gap 
    time.sleep(1) # wait a second 
  ```
 
### Reflection

This was the first part of the Crash Avoidance assignment. I have never used accelerometer so I wasn't sure how to start. The canvas page was very helpful and gave me a link to see how to write f-strings, so after reading about how to wrote that code I was able to figure it out. My code wasn't working in the beginning but I got some help and realized I used the wrong bracket. After I fixed that the code worked. 
