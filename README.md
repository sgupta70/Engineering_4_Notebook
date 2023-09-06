# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry_Pi_Assignment_Template](#raspberry_pi_assignment_template)
* [Onshape_Assignment_Template](#onshape_assignment_template)

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

For this assignment we had to get a Raspberry Pi Pico to blink 
### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

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
Give me a link to your code. [Something like this](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). Don't make me hunt through your folders, give me a nice link to click to take me there! Remember to **COMMENT YOUR CODE** if you want full credit. 

### Reflection

A majority of this assignment was getting our computers set up and connecting VS Code with Github. The code part was very simple, there was no wiring the 

