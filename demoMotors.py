from random import randint, seed
from gpiozero import Motor, Button
import time

old_x = 5
old_size = 5
new_x = 5
new_size = 5
seed(1)
front = None
side = None

motor1 = Motor(25, 22)
motor2 = Motor(24, 23)
motor3 = Motor(10, 9)
motor4 = Motor(16, 26)
limit_switch = Button(17)
power_switch = Button(4)


def north():
    motor1.forward()
    motor2.forward()
    motor3.forward()
    motor4.forward()
    print("north")


def northeast():
    motor1.stop()
    motor2.forward()
    motor3.forward()
    motor4.stop()
    print("northeast")


def east():
    motor1.backward()
    motor2.forward()
    motor3.forward()
    motor4.backward()
    print("east")


def southeast():
    motor1.backward()
    motor2.stop()
    motor3.stop()
    motor4.backward()
    print("southeast")


def south():
    motor1.backward()
    motor2.backward()
    motor3.backward()
    motor4.backward()
    print("south")


def southwest():
    motor1.stop()
    motor2.backward()
    motor3.backward()
    motor4.stop()
    print("southwest")


def west():
    motor1.forward()
    motor2.backward()
    motor3.backward()
    motor4.forward()
    print("west")


def northwest():
    motor1.forward()
    motor2.stop()
    motor3.stop()
    motor4.forward()
    print("northwest")


def stop():
    motor1.stop()
    motor2.stop()
    motor3.stop()
    motor4.stop()
    print("stop")


while True:
    while power_switch.value == 1:
        new_x = randint(0, 10)
        new_size = randint(0, 10)
        print("Old x: " + str(old_x) + "|New x: " + str(new_x))
        print("Old size: " + str(old_size) + "|New size: " + str(new_size))

        front = new_size - old_size
        side = new_x - old_x
        print("Front: " + str(front) + " |Side: " + str(side))

        if limit_switch.value:
            print("triggered")
            stop()
            time.sleep(5)
            print("pause over")
            continue

        if front > 0:
            if side > 0:
                northeast()
            elif side < 0:
                northwest()
            else:
                north()
        elif front < 0:
            if side > 0:
                southeast()
            elif side < 0:
                southwest()
            else:
                south()
        else:
            if side > 0:
                east()
            elif side < 0:
                west()
            else:
                stop()

        old_x = new_x
        old_size = new_size
        time.sleep(2)
    break
motor4.close()
motor3.close()
motor2.close()
motor1.close()
limit_switch.close()
power_switch.close()
