from random import randint, seed
from gpiozero import Motor
import RPi.GPIO as GPIO
import time

# TODO: need to plug in motors and find pins
# setting up motors
motor1 = Motor(1, 2)  # top right motor
motor2 = Motor(1, 2)  # top left motor
motor3 = Motor(1, 2)  # bottom right motor
motor4 = Motor(1, 2)  # bottom left motor

# TODO: need to find pins for GPIO
# setting up GPIO pins for limit and power switch
limit_switch = 3
power_switch = 4
rst_button = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(power_switch, GPIO.IN)
GPIO.setup(limit_switch, GPIO.IN)
GPIO.setup(rst_button, GPIO.IN)

# setting up variables
old_x = 5
old_size = 5
new_x = 5
new_size = 5
seed(1)
front = None
side = None


# defining functions for directional movements
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
    motor4, stop()
    print("stop")


# surrounding while true loop in try loop
# to exit when reset button is pressed
try:
    while True:
        # while the power switch is on, the car will move
        while GPIO.input(power_switch):
            # if the limit switches are triggered the car will stop
            if GPIO.input(limit_switch):
                time.sleep(10)

            # creating random new x and size variable to mimic camera input
            new_x = randint(0, 10)
            new_size = randint(0, 10)
            # printing to debug
            print("Old x: " + str(old_x) + "|New x: " + str(new_x))
            print("Old size: " + str(old_size) + "|New size: " + str(new_size))

            # comparing new to old
            front = new_size - old_size
            side = new_x - old_x
            print("Front: " + str(front) + " |Side: " + str(side))

            # conditionals to set direction
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

            # updating old x and size variables
            old_x = new_x
            old_size = new_size
            # sleeping for 2 seconds to let the motor actually move
            time.sleep(2)
# using reset button to exit code
except GPIO.input(rst_button):
    exit()
