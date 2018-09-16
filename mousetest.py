# mousetest.py
import pyautogui as pya

print(pya.size())
pya.moveTo(10,10, duration=0.5)
#pya.scroll(5)
pya.typewrite(['l','s', 'enter'])

# this file was used to test the pya functions