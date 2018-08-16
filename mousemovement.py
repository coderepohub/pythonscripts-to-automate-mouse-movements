import pyautogui
import time
///Infinite loop
while(True):
    pyautogui.moveTo(500, 400, duration= 1)
    pyautogui.moveRel(0, 340, duration=2)
    time.sleep(5)
    pyautogui.moveTo(700, 300, duration= 1)
    pyautogui.click(700, 300)
    time.sleep(50)


