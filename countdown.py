#type: ignore 

import board 
import digitalio 
import time 

while True: 
  for x in range(10, 0, -1): # in the range from 10 to 0 going down by 1
     time.sleep(0.5) # wait a second 
     print(x) # print the variable
    time.sleep(0.5) # wait 2 seconds 
     print("launch")