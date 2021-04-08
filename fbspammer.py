#INSTALL PYAUTOGUI: pip install pyautogui
import pyautogui
import time

#ENTER CUSTOM TEXT 
message = ":)"
#HOW MANY TIMES
n = 30

print("START")

count = 3
while(count != 0):
    time.sleep(1)
    count -= 1

print("\n END")

for i in range(0, int(n)):
    pyautogui.typewrite(message + "\n")