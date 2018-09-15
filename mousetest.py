# mousetest.py
import pyautogui as pya

print(pya.size())
pya.moveTo(10,10, duration=0.5)
#pya.scroll(5)
pya.typewrite(['l','s', 'enter'])