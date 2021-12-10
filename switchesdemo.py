from gpiozero import Button
import time

limit_switch = Button(3)
power_switch = Button(4)
reset_button = Button(5)

while True:
    if limit_switch.value == 0:
        print("limit switch triggered")
    if power_switch.value == 1:
        print("power switch is on")
    if  reset_button == 1:
        print("reset button was pressed")
    time.sleep(2)
