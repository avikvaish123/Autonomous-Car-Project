from gpiozero import Motor
import RPi.GPIO as GPIO
import time

# TODO: import camera and cv libraries

# set up for pins for external controls
limit_switch = 3
power_switch = 4
reset_button = 5

# variable to keep track of image pos and size
old_x = 0
old_size = 0
new_x = 0
new_size = 0
front = None
side = None

# setting up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(limit_switch, GPIO.IN)
GPIO.setup(power_switch, GPIO.IN)
GPIO.setup(reset_button, GPIO.IN)

# setting up motor pins
motor1 = Motor(4, 14)
motor2 = Motor(11, 27)
motor3 = Motor(5, 15)
motor4 = Motor(12, 28)


# TODO: need to setup the camera and initialize it


# functions for movement
def north():
    motor1.forward()
    motor2.backward()
    motor3.backward()
    motor4.forward()


def northeast():
    motor1.forward()
    motor2.stop()
    motor3.backward()
    motor4.stop()


def east():
    motor1.forward()
    motor2.forward()
    motor3.backward()
    motor4.backward()


def southeast():
    motor1.stop()
    motor2.forward()
    motor3.stop()
    motor4.backward()


def south():
    motor1.backward()
    motor2.forward()
    motor3.forward()
    motor4.backward()


def southwest():
    motor1.backward()
    motor2.stop()
    motor3.forward()
    motor4.stop()


def west():
    motor1.backward()
    motor2.backward()
    motor3.forward()
    motor4.forward()


def northwest():
    motor1.stop()
    motor2.backward()
    motor3.stop()
    motor4.forward()


def stop_motors():
    motor1.stop()
    motor2.stop()
    motor3.stop()
    motor4.stop()


# TODO: get first image and store into old image
# TODO: get first x position and size

while True:
    if GPIO.input(power_switch):
        if GPIO.input(limit_switch):
            stop_motors()
            time.sleep(5)
        if GPIO.input(reset_button):
            break
        # TODO: get new image, x position and size

        if new_x > old_x:
            side = 1
        elif new_x == old_x:
            side = 0
        else:
            side = -1

        if old_size > new_size:
            front = 1
        elif old_size > new_size:
            front = 0
        else:
            front = -1

        if front > 0:
            if side == 1:
                northeast()
            elif side == 0:
                north()
            else:
                northwest()
        elif front < 0:
            if side == 1:
                southeast()
            elif side == 0:
                south()
            else:
                southwest()
        else:
            if side == 1:
                east()
            elif side == -1:
                west()
            else:
                stop_motors()

        old_x = new_x
        old_size = new_size
        time.sleep(1)
