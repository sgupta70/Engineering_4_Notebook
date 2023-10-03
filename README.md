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

This assignment wasn't very hard, I used the range() function which was something I hasn't used in a while so I had to re-learn how to use it. Using a sight online I read more about it and understood what I had to do to get the serial monitor to print a countdown. Overall it was a good assignment to get back into code. 

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

This assignment wasn't super hard. I used the code from the part above and then added what I knew about LEDS from last year to turn the green and red LED  on at the correct times.  

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

## Part 2

### Assignment Description

For this assignment we had to add on to what we did above and get an LED to light up when it is tilted 90 degress to either side and also wire up a JST battery so it can run without being connected to the computer. I used an if statement to turn on the LED when the accelerometer printed out a z value of 90 degrees.

### Evidence 

![My Project (3)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/65fec802-1e97-471b-b25c-d1711adbe4d3)

### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/e487c724-7d94-43ce-ad2d-34ec5806a160)

### Code
```
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
  ```
 
### Reflection
I was able to just use my code from part 1 and just add on an if statement and define the LED. I read some about if statements to remember how to do them and once I did I was able to writ eone. It was working but the light kept flashing when it was horizontal so I switched the signs and the when the LED would be True(on) and False(off). Overall this assignment wasn't too bad and it was good to do if statements again. 

## Part 3

### Assignment Description

This was the last part of the crash avoidance assignment. We had to put all three parts together and get the x, y, and z values to print out on a OLED screen.

### Evidence 

![My Project (7)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/85cc5ef4-1fa6-453a-a591-f5a9e6ec52ae)

### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/a7f67a0b-b5e7-4dbe-98ec-b1d3fa155a8b)

### Code
```
#type: ignore 

import board 
import digitalio
import time
import adafruit_mpu6050
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio 
import displayio


displayio.release_displays()
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(board.GP15, board.GP14)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP3)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)


led = digitalio.DigitalInOut(board.GP0) 
led.direction = digitalio.Direction.OUTPUT 
mpu = adafruit_mpu6050.MPU6050(i2c, address=0X68)
print(mpu.acceleration) 

# create the display group
splash = displayio.Group()

# add title block to display group
title = "ANGULAR VELOCITY"
# the order of this command is (font, text, text color, and location)
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    

# you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
# Don't forget to round the angular velocity values to three decimal places

# send display group to screen
display.show(splash)

while True:   
    mpu.gyro
    text_area.text = (f"ANGULAR VELOCITY ) \nx : {mpu.acceleration[0]} \ny : {mpu.acceleration[1]} \nz :  {mpu.acceleration[2]}") # prints the values of x,y and z on the screen

    led.value = False # led is off 

    if mpu.acceleration[0] > 9 or mpu.acceleration[0] < -9:
        print("no light") # print that the light is not on 
        led.value = True # led is on if it is tilted to 90 degress

  ```
 
### Reflection
This last part wasn't too bad, I was able to figure out how to write the code to print the values out on the screen, but when I tried uploading it wouldn't work. I got some help and we realized I just had a very sensitive wire so I just had to be careful not to mess up that wire so it wouldn't disconnect. After fixing that the code uploaded and it worked. Overall this assignment wasn't too bad it was good to continue getting back into code and trying new things I haven't coded yet. I learned how to code an OLED screen and throughout this assignment I learned how to use f-strings. I am now excited to start CAD!


## FEA_Part_1 

### Assignment Description
For this assignement we were partnered up and required to make the strongest beam we could with any prior knowledge. They would then be tested as we add weight to a bucket. The bucket had to hang 180mm away from the base and it had to weight a maximum of 13 grams.  

### Part Link 

[Link to OnShape Document](https://cvilleschools.onshape.com/documents/8b325fcbf1fc9ced667a46ad/w/244fda1d4dd423e6920295c5/e/da5820986e36d6e64f72469d?renderMode=0&uiState=651c4898682dbd1154ff7054)

### Part Image

![Beam Starter + Holder (1)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/e544fb58-9bc6-48a1-bf78-4421a7003cab)
![Beam Starter + Holder](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/6d120254-8b42-4404-98a4-d1a67529a0ab)


### Reflection

When starting this assignment we had the idea to make a I beam because it seemed to be the strongest, however we realized that there would be a lot of overhang and the beam would not be able to print. So we pivoted our idea and realized that triangles are the strongest shape. We made a long triangular prism with supporting beams inside. It matched the requirement for 180mm but it was too heavy. WE had to make the walls a lot thinner and cut out a lot of holes so it would be 13 grams. Overall this assignment was fun and a good way to get back into CAD and we can't wait to see how well it works. 
