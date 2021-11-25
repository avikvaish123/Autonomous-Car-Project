import time
from gpiozero import Motor

# TODO: need to figure out pins for motors
motor1 = Motor(4, 14)
motor2 = Motor(3, 27)
motor3 = Motor(5, 13)
motor4 = Motor(6, 18)


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


counter = 0

while True:
    print(counter)
    mod9 = counter % 8
    if mod9 == 0:
        north()
        print("north")
    elif mod9 == 1:
        northeast()
        print("northeast")
    elif mod9 == 2:
        east()
        print("east")
    elif mod9 == 3:
        southeast()
        print("southeast")
    elif mod9 == 4:
        south()
        print("south")
    elif mod9 == 5:
        southwest()
        print("southwest")
    elif mod9 == 6:
        west()
        print("west")
    elif mod9 == 7:
        northwest()
        print("northwest")
    else:
        stop_motors()
        print("stopped")

    counter = counter + 1

    time.sleep(2)
