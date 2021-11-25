import time


def north():
    print("north")


def south():
    print("south")


def east():
    print("east")


def west():
    print("west")


def stop_motors():
    print("stop")


counter = 0

while True:
    print(counter)
    if counter == 20:
        break

    mod5 = counter % 5
    print(mod5)

    if mod5 == 0:
        north()
    elif mod5 == 1:
        east()
    elif mod5 == 2:
        south()
    elif mod5 == 3:
        west()
    else:
        stop_motors()

    counter = counter + 1
    time.sleep(2)
