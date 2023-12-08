# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)
* [LED_Blink](#led_blink)
* [Launch_Pad_Assignment](#launch_pad_assignment)
* [Crash_Avoidance_Assignment](#crash_avoidance_assignment)
* [Landing_Area_Assignment](#landing_area_assignment)
* [Morse_Code](#morse_code)
* [Data_Storage](#data_storage)
* [FEA_Beam](#fea_beam)



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


# Code

## LED_Blink

#### Assignment Description

For this assignment we had to set up our VS Code so it would be connected to GitHub and get a Raspberry Pi Pico to blink.

#### Evidence 

![ezgif com-crop](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/0ac23d86-3241-46a1-bcbd-60724e039f2f)


#### Wiring

No wiring, plugged right into the computer 

#### Code
```
import board 
import digitalio 
import time 

led = digitalio.DigitalInOut(board.LED) 
led.direction = digitalio.Direction.OUTPUT 

while True: 
    led.value = True # turn led on
    time.sleep(0.5) # wait a half second 
    led.value = False # turn led off
    time.sleep(0.5) # wait a half second 
  ```
 [Code](https://github.com/sgupta70/Engineering_4_Notebook/blob/main/LED_blink.py)
 
#### Reflection

A majority of this assignment was getting our computers set up and connecting VS Code with Github. The code part was very simple, there was no wiring needed so the pico was plugged right into the computer. The code would just turn the LED on and off. It was super simple and a good way to get back into coding for the new year. 

## Launch_Pad_Assignment

### Part 1 

#### Assignment Description

For this assignment we had to get our serial monitor to print a countdown which was counting down from 10

#### Evidence 

![ezgif com-optimize (1)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/91e85500-1036-4b44-96cc-9e324c315a18)

#### Wiring

No wiring, plugged right into the computer 

#### Code
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
 
#### Reflection

This assignment wasn't very hard, I used the range() function which was something I hasn't used in a while so I had to re-learn how to use it. Using a sight online I read more about it and understood what I had to do to get the serial monitor to print a countdown. Overall it was a good assignment to get back into code. 

### Part 2

#### Assignment Description

For this part we had to get two LEDs to blink with the countdown, flashing red as it counts down from ten and then turns green when it prints "launch". 

#### Evidence 

![ezgif com-resize](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/8bf5a4a4-6273-4a8b-92cc-04161d98ef88)


#### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/9273f53b-699c-46c2-ab94-15fcf7f62ce8)


#### Code
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
    ledRed.value = True # turn red led on
    time.sleep(0.5)
    ledRed.value = False # turn red led off 
    time.sleep(0.5) # blink red led
print("Launch")
ledGreen.value = True # turn green led on
time.sleep(5.0) # green led on for 5 secs
    
  ```
 
#### Reflection

This assignment wasn't super hard. I used the code from the part above and then added what I knew about LEDS from last year to turn the green and red LED  on at the correct times. I wired up both of the LEDs and nmed one Red and Green so I didn't get confused and I was able to just put it into the cide because I remembered how to turn on an LED from past assignments.

### Part 3

#### Assignment Description

For this part we had to press a button which would then get two LEDs to blink with the countdown, flashing red as it counts down from ten and then turns green when it prints "launch". 

#### Evidence 

![ezgif com-optimize](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/384cad2e-5eac-4729-a733-671b42b083fc)


#### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/1d8b4772-412d-4ca4-b1e0-0f1792f9279d) 

#### Code
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
                ledRed.value = True # turn red led on
                time.sleep(0.5)
                ledRed.value = False # turn red led off 
                time.sleep(0.5)
            ledGreen.value = True # turn green led on 
            print("Launch") 
            time.sleep(3.0)
            ledGreen.value = False # turn green led off 
        else:
            print("Button is up")

    prev_state = cur_state # reset button value 
  ```
 
#### Reflection

This assignment wasn't super hard using my knowledge from last year I knew how to get a button to work. I just put the code for the button into my existing code from part 2. In the beginning the code wouldn't load onto the pico but I figured it out and realized it wasn't uploading to the D drive so once I fixed that it worked. 

### Part 4

#### Assignment Description

For this part we had to press a button which would then get two LEDs to blink with the countdown, flashing red as it counts down from ten and then turns green and moves the servo when it "launches". 

#### Evidence 

![ezgif com-optimize (3)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/d730d765-c9b4-47cd-9032-c1acf9051cdc)


#### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/82896b62-b3e1-4695-90cc-4005b2729d48)

#### Code
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
            print("button pressed")
            for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
                print(x) # print the variable
                ledRed.value = True # turn red led on
                time.sleep(0.5)
                ledRed.value = False # turn red led off
                time.sleep(0.5) 
            ledGreen.value = True # turn green led on
            print("Launch")
            for angle in range(0, 180, 1):  # 0 - 180 degrees, 1 degrees at a time.
                my_servo.angle = angle
                time.sleep(0.05)
            time.sleep(3.0)
            ledGreen.value = False # turn on green light and print launch then turn the light off after 3 seconds
            for angle in range(180, 0, -1): # 180 - 0 degrees, 1 degrees at a time.
                my_servo.angle = angle # bring servo back to reset
            time.sleep(0.05)
        else:
            print("button done")

    prev_state = cur_state # reset button value
  ```
 
#### Reflection

This was the final part for this assignment, I used to code that I already had and added in code for a servo which I remembered from last year. It wasn't working and we realized that one of my wires wasn't going into the correct pin so after switching that it all worked together. This assignment was a good way to get into code. 


## Crash_Avoidance_Assignment

### Part 1 

#### Assignment Description

For this assignment we had to wire up an accelerometer and get it to print out the x, y, and z values on the serial monitor. 

#### Evidence 

![ezgif com-crop (3)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/8844d422-a745-4fed-9fba-417db9241eea)

#### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/f3594102-ce2c-4bd0-8c28-24206cadcea1)

#### Code
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
 
#### Reflection

This was the first part of the Crash Avoidance assignment. I have never used accelerometer so I wasn't sure how to start. The canvas page was very helpful and gave me a link to see how to write f-strings, so after reading about how to wrote that code I was able to figure it out. My code wasn't working in the beginning but I got some help and realized I used the wrong bracket. After I fixed that the code worked. 

### Part 2

#### Assignment Description

For this assignment we had to add on to what we did above and get an LED to light up when it is tilted 90 degress to either side and also wire up a JST battery so it can run without being connected to the computer. I used an if statement to turn on the LED when the accelerometer printed out a z value of 90 degrees.

#### Evidence 

![My Project (3)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/65fec802-1e97-471b-b25c-d1711adbe4d3)

#### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/e487c724-7d94-43ce-ad2d-34ec5806a160)

#### Code
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
 
#### Reflection
I was able to just use my code from part 1 and just add on an if statement and define the LED. I read some about if statements to remember how to do them and once I did I was able to writ eone. It was working but the light kept flashing when it was horizontal so I switched the signs and the when the LED would be True(on) and False(off). Overall this assignment wasn't too bad and it was good to do if statements again. 

### Part 3

#### Assignment Description

This was the last part of the crash avoidance assignment. We had to put all three parts together and get the x, y, and z values to print out on a OLED screen.

#### Evidence 

![My Project (7)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/85cc5ef4-1fa6-453a-a591-f5a9e6ec52ae)

#### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/a7f67a0b-b5e7-4dbe-98ec-b1d3fa155a8b)

#### Code
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

display.show(splash) # send display group to screen

while True:   
    mpu.gyro
    text_area.text = (f"ANGULAR VELOCITY ) \nx : {mpu.acceleration[0]} \ny : {mpu.acceleration[1]} \nz :  {mpu.acceleration[2]}") # prints the values of x,y and z on the screen

    led.value = False # led is off 

    if mpu.acceleration[0] > 9 or mpu.acceleration[0] < -9:
        print("no light") # print that the light is not on 
        led.value = True # led is on if it is tilted to 90 degress

  ```
 
#### Reflection
This last part wasn't too bad, I was able to figure out how to write the code to print the values out on the screen, but when I tried uploading it wouldn't work. I got some help and we realized I just had a very sensitive wire so I just had to be careful not to mess up that wire so it wouldn't disconnect. After fixing that the code uploaded and it worked. Overall this assignment wasn't too bad it was good to continue getting back into code and trying new things I haven't coded yet. I learned how to code an OLED screen and throughout this assignment I learned how to use f-strings. I am now excited to start CAD!

## Landing_Area_Assignment 

### Part 1

#### Assignment Description

For this assignment we had to write a script that takes three coordinates and returns the area using a function.

#### Evidence 

![Capture](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/e2ffc129-f073-443c-8d92-a91eca0a0704)

#### Wiring

none 

#### Code
```
import time

def validate_input(input_string: str): # return false on error or an array of the form [x, y]
    try:
        input_parts = input_string.split(",") 
    except ValueError:
        return False
    if len(input_parts) != 2: # we expect an x and a y coordinate
        return False
    try:
        result = [float(part) for part in input_parts] # turn the strings in input_parts into floats
        return result
    except ValueError:
        return False

def get_area(p1, p2, p3): 
    area = 0.5 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) # find area 
    return abs(area)

while True:
    vertex_1 = validate_input(input("Vertex 1: "))
    if not vertex_1:
        print("Not Correct, try again.")# print error if doesn't work 
        continue    
    vertex_2 = validate_input(input("Vertex 2: "))
    if not vertex_2:
        print("Not Correct, try again."")
        continue
    vertex_3 = validate_input(input("Vertex 3: "))
    if not vertex_3:
        print("Not Correct, try again."")
        continue
    area = get_area(vertex_1, vertex_2, vertex_3)   # put points into area equation 
    print(f"The area of the triangle with vertices ({vertex_1[0]},{vertex_1[1]}), ({vertex_2[0]},{vertex_2[1]}), ({vertex_3[0]},{vertex_3[1]}) is {area} square km.")
  ```
 
#### Reflection
This assignment was too bad, getting help from the people next to me and using parts of [River's code](https://github.com/rivques) code, I was able to easily trouble shoot and see why it wasn't working. My biggest problem was that it was just loading very slowly so it took forever to type in the coordinates but it worked well and printed out what I needed. 

### Part 2

#### Assignment Description

For this assignment we had to write a script that takes three coordinates and returns the area using a function and plot the triangle on a onboard OLED screen relative to the base location.

#### Evidence 

![My Project (8)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/a8b41497-9122-45f5-af16-3032adc9cfe4)

#### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/5297f943-18ff-4571-9100-8adf44b70285)


#### Code
```
#type: ignore

import time
import terminalio
import displayio
import busio    
import board
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.line import Line


# init displays
displayio.release_displays()

# init i2c
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP3)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

splash = displayio.Group()

splash.append(Circle(64, 32, 3, outline=0xFFFFFF))
splash.append(Line(0, 32, 128, 32, 0xFFFFFF))
splash.append(Line(64, 0, 64, 64, 0xFFFFFF))
area_label = label.Label(terminalio.FONT, x=5, y=5, text="")
splash.append(area_label)
landing_area_display = None
display.show(splash)

def validate_input(input_string: str): # return false on error or an array of the form [x, y]
    try:
        input_parts = input_string.split(",")
    except ValueError:
        return False
    if len(input_parts) != 2: # we expect an x and a y coordinate
        return False
    try:
        result = [float(part) for part in input_parts] 
        return result
    except ValueError: 
        return False

def get_area(p1, p2, p3):
    area = 0.5 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
    return abs(area)

while True:
    vertex_1 = validate_input(input("Please input three triangle vertices in x,y format. Vertex 1: "))
    if not vertex_1:
        print("Not Correct, try again.") # if the format doesn't work print this
        continue
    vertex_2 = validate_input(input("Vertex 2: "))
    if not vertex_2:
        print("Not Correct, try again."")
        continue
    vertex_3 = validate_input(input("Vertex 3: "))
    if not vertex_3:
        print("Not Correct, try again."")
        continue
    area = get_area(vertex_1, vertex_2, vertex_3) # put points into area equation 
    print(f"The area of the triangle with vertices ({vertex_1[0]},{vertex_1[1]}), ({vertex_2[0]},{vertex_2[1]}), ({vertex_3[0]},{vertex_3[1]}) is {area} square km.")
    area_label.text = f"{area:.2f}km2" # set the text that shows on the display
    if landing_area_display is not None: # get rid of triangle if there was one 
        splash.pop()
    landing_area_display = Triangle(int(vertex_1[0])+64, 32-int(vertex_1[1]), int(vertex_2[0])+64, 32-int(vertex_2[1]), int(vertex_3[0])+64, 32-int(vertex_3[1]), outline=0xFFFFFF)
    splash.append(landing_area_display) # print the new triangle
```
 
#### Reflection
This assignment was just adding on from what we did above so the code wasn't bad. We already wired an OLED screen so I didn't need to fix my wiring at all and I had some code from that assignment so I knew how to turn it on and get it to print. I added lines from my previous OLED assignment and with some help from my the people sitting next to me and using parts of [River's code](https://github.com/rivques) code, I was able to finish this assignment.
## Morse_Code

### Part 1

#### Assignment Description

For this assignment we had to write a morse code translator and print those dots and dashes to the serial monitor. The script must accept text input and if you type anything else, your script must translate the text to morse code dots and dashes, and print those to the monitor. The printed text must use a space to show breaks between letters, and a slash to show breaks between words. I used large portions of Rivers's work in this assignment. [Here is a link to their notebook](https://github.com/rivques)


#### Evidence 

![My Project (9)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/c77db802-484d-41cf-8e41-4baa16e4594d)

#### Wiring

none

#### Code
```

import time

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'} # numbers and letters tasnlated to morse code 
while True:
    user_input = input("Enter the string to translate, or type '-q' to quit. ") 
    user_input = user_input.upper()
    if user_input == "-q":
        break #everything stops if you type -q in
    morse = ""
    translationworks = True
    for letter in user_input:
        if letter == " ":
            morse += "/" #if you put a space it will make a break 
        else:
            try:
                morse += MORSE_CODE[letter] + " "
            except KeyError:
                print(f"Unsupported character \"{letter}\" used. Please try again.") #if you put in a letter that can't work it will tell you
                translationworks = False
                break
    if translationworks:
        print(morse_translation) # print out the word in morse code 
            
print("done")

```
 
#### Reflection
This was the first time I have used morse code, but we were given the dictionary which was really nice. The code wasn't bad because it was just if statements and I learned to make a space you use += instead of just =. With the help from my neighbors I was able to get my code up and running.

### Part 2

#### Assignment Description

For this assignment we had to add onto the assignment before, after getting the morse code to print on the serial monitor I had to get the morse code to flash on the led. 

#### Evidence 

![My Project (10)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/13c28976-d3d9-41a6-ad45-238896a0f067)

#### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/910b2bb8-0885-423c-a6e0-61c47d446fae)

#### Code
```

# type: ignore

import board
import digitalio
import time

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'} # letters and numbers in morse code 

led = digitalio.DigitalInOut(board.GP14) # led as an output on GP14
led.direction = digitalio.Direction.OUTPUT 

modifier = 0.25 # base delay for led

delayz = {
    ".": 1*modifier,
    "-": 3*modifier,
    " ": 3*modifier,
    "/": 7*modifier # time in between flashes for each character
}

while True:
    user_input = input("Enter the string to translate, or type '-x' to quit. ")
    user_input = user_input.upper() # lowercase to uppercase
    if user_input == "-X": # uppercase because of the previous line
        break # if you input x it quits
    morse_translation = ""
    translation_good = True # translation is correct 
    for letter in user_input:
        if letter == " ":
            morse_translation += "/" # a space in the input translates to a break 
        else:
            try:
                morse_translation += MORSE_CODE[letter] + " " # for spaces between characters
            except KeyError:
                print(f"Unsupported character \"{letter}\" used.") # print if theres something wrong
                translation_good = False
                break # go to next line
    if translation_good:
        print(morse_translation) # print the translation is everything looks good
        for character in morse_translation:
            on_delay = delayz[character]
            off_delay = delayz[character] # import the delays from the if statement
            if on_delay == 0:
                time.sleep(off_delay) # led if off if there is nothing typed 
            else:
                led.value = True
                time.sleep(on_delay)
                led.value = False
                time.sleep(off_delay) 

```
 
#### Reflection
This assignment wasn't that bad, I used the code from the assignment before and then I already knew how to code an LED, the only difficult thing was to get the LED to either blink or flash which I got help from google and my neighbors. The wiring was super simple because I've wired an LED so many times. Overall this assignment wasn't bad and it was fun to learn morse code. I used large portions of Rivers's work in this assignment. [Here is a link to their notebook](https://github.com/rivques)


## Data_Storage

### Part 1

#### Assignment Description

For this year our project is to launch a Pi into the sky and get it to record data so this assignment helped us learn how to save the data when it is not plugged into the computer. We needed to take data from your accelerometer, store it onboard the Pico, and then open it on your computer. 

#### Evidence 

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/3f8b8a65-b36a-4644-ac1e-987284b63d94)

#### Wiring

![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/6494bacc-6dc1-4517-8f67-7a7731217999)

#### Code
```
# type: ignore
# libraries: adafruit_mpu6050.mpy | adafruit_bus_device | adafruit_register
import adafruit_mpu6050
import busio
import board
import time
import digitalio
import displayio
import storage # imports

displayio.release_displays() # this needs to be first in the code

led1 = digitalio.DigitalInOut(board.GP1) 
led1.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin) 
mpu = adafruit_mpu6050.MPU6050(i2c) # set up for variables and pin locations

while True: 
    acc = mpu.acceleration
    print(f"X: {acc[0]}m/s² Y: {acc[1]}m/s² Z: {acc[2]}m/s²") # f string for accel of the breadboard
    time.sleep(0.25)
    led1.value = False # default led is off
    if abs(acc[2]) < 2:
        led1.value = True # led turns on 
    if not storage.getmount("/").readonly: # call back to the boot.py file
        with open("/data.csv", "a") as datalog:
            time_elapsed = time.monotonic()
            csv_string = f"{time_elapsed},{acc[0]},{acc[1]},{acc[2]},{led1.value}\n"
            # f string showing time, acc, and whether or not it's tilted
            datalog.write(csv_string)
            led1.value = True # led turns on
            time.sleep(0.1)
            led1.value = False # led turns off 
            time.sleep(0.1) # led blink to show switch between settings 
            datalog.flush() # record to the datalog
            time.sleep(0.25)
    else:
        time.sleep(0.25)

```
 
#### Reflection
This assignment was too bad because we already had most of the code written from the Crash Avoidance assignment. The boot.py code was already given to us and I needed to make sure to save it correctly because that allows you to switch from "code" to "data" mode. When it is in data mode you can collet data when it is unplugged and it code mode you can edit the code. There wasn't a ton of code towrite I just needed to understand how to collect the data and then open in up in an EXCEL. I also got help from the people sitting next to me to put my f" strings into one, and I got help from [Cooper's code](ttps://github.com/Cooper-Moreland)

### Part 2 

#### Assignment Description
For this part all we needed to do was grpah the x, y and z values on a line graph and the when the pico was tilted/when the led was on on a column graph. 

#### Evidence 
![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/24e63a8e-1529-475e-bcc1-a4b71320a021)
![image](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/1f5b63b4-aaae-4e65-b7ea-8db12b208f7a)

#### Code 
none 

#### Wiring 
none 

#### Reflection 
This part wasn't hard all I needed to do was graph the data I already had stored. I was able to copy and paste it over to google sheets and use their charts to make my two graphs. 

# CAD

## FEA_Beam

### FEA_Part_1 

#### Assignment Description
For this assignement we were partnered up and required to make the strongest beam we could with any prior knowledge. They would then be tested as we add weight to a bucket. The bucket had to hang 180mm away from the base and it had to weight a maximum of 13 grams.  

#### Part Link 

[Link to OnShape Document](https://cvilleschools.onshape.com/documents/8b325fcbf1fc9ced667a46ad/w/244fda1d4dd423e6920295c5/e/da5820986e36d6e64f72469d?renderMode=0&uiState=651c4898682dbd1154ff7054)

#### Part Image

![Beam Starter + Holder (1)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/e544fb58-9bc6-48a1-bf78-4421a7003cab)
![Beam Starter + Holder](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/6d120254-8b42-4404-98a4-d1a67529a0ab)


#### Reflection

When starting this assignment we had the idea to make a I beam because it seemed to be the strongest, however we realized that there would be a lot of overhang and the beam would not be able to print. So we pivoted our idea and realized that triangles are the strongest shape. We made a long triangular prism with supporting beams inside. It matched the requirement for 180mm but it was too heavy. WE had to make the walls a lot thinner and cut out a lot of holes so it would be 13 grams. Overall this assignment was fun and a good way to get back into CAD and we can't wait to see how well it works. 


### FEA_Part_2/3

#### Assignment Description
We learned how to do a simulation on Onshape called FEA which shows the weakest and strongest parts of a desgin when force is applied. 

#### Part Link 

[Link to OnShape Document](https://cvilleschools.onshape.com/documents/8b325fcbf1fc9ced667a46ad/w/244fda1d4dd423e6920295c5/e/da5820986e36d6e64f72469d?renderMode=0&uiState=651c4898682dbd1154ff7054)

#### Part Image
![Assembly 1 (1)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/39202830-fd05-4bbc-83b5-1d62d99b433c)
![Assembly 1 (2)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/4f51f6cd-e556-4d24-a891-ead528de8e5b)
![Assembly 1](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/25e762aa-cc76-4c3b-a7d2-02801b0c0838)
![Assembly 1 (3)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/f193720c-f05c-4be0-8003-15ed7fc8370f)


#### Reflection

Our design is very good with most of the stress being at the point that connects to the base. The structural beams inside where very helpful to support the fore. We just need to reinforce the points of the triangle that are close to the base so it doesn't snap. 

### FEA_Part_4

#### Assignment Description

After knowing the weakest points in our design we had to work to make it better to haave less displacement in our beam for the areas that the FEA simulation showed were weak.

#### Part Link 

[Link to OnShape Document](https://cvilleschools.onshape.com/documents/8b325fcbf1fc9ced667a46ad/w/244fda1d4dd423e6920295c5/e/da5820986e36d6e64f72469d?renderMode=0&uiState=651c4898682dbd1154ff7054)

#### Part Image

![Assembly 1 (5)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/6edb8424-2db6-4bd4-a8f1-5fa8272c07fb)
![Assembly 1 (9)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/d17533c0-c10e-4da3-bf17-ea3c5950bb66)
![Assembly 1 (7)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/32fb9931-31da-4c16-9570-4ea3a329bba5)
![Assembly 1 (10)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/3d8094fd-4755-4261-8f7d-98da82d39743)
![Assembly 1 (8)](https://github.com/sgupta70/Engineering_4_Notebook/assets/71406903/8eacc8b7-5bf5-438b-a693-ea49dab8aee9)

#### Reflection

Our beam was already pretty good with not a lot of yellow so it was kind of hard to improve. To improve our beam we added more support to the walls closest the the holder, so it wouldn't break as easily. We also thickend some of the walls were there was the most yellow. Doing that added more weight so we had to create more holes to remove the weight. We hope that this will improve our beam and overall it was a fun project!


