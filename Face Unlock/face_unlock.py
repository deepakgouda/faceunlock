import pyautogui
import time
import os

time.sleep(1)
access_file=open('access.txt','r')
access=access_file.read()
if access == "True":
	# Put your password here.
    pyautogui.typewrite('Your Password Here')
    pyautogui.press('enter')