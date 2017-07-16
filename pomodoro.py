import webbrowser
import time
import ctypes

print"This program started on "+time.ctime()

def focused_mode():
    minutes = 25
    t = minutes * 60
    time.sleep(t)
    ctypes.windll.user32.MessageBoxA(0, "Please take a break, you deserve it!!!!", "Break", 1)

def diffused_mode_short():
    minutes = 5
    t = minutes * 60
    time.sleep(t)
    ctypes.windll.user32.MessageBoxA(0, "Your short break is over, time to get back to work!!", "Work", 1)

def diffused_mode_long():
    minutes = 15
    t = minutes * 60
    time.sleep(t)
    ctypes.windll.user32.MessageBoxA(0, "Your long break is over, time to get back to work!!", "Work", 1)

for i in range(1,200):
    focused_mode()
    if i % 4 == 0:
        diffused_mode_long()
    else:
        diffused_mode_short()
