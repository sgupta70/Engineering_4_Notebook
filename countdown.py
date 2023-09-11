#type: ignore 

import board 
import digitalio 
import time 

while True: 
  for x in range(10, 0, -1):
     time.sleep(0.5)
     print(x)
    time.sleep(0.5)
     print("launch")