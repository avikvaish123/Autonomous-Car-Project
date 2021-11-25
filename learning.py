import time
from random import seed
from random import randint

old_x = 5
old_size = 5
new_x = 5
new_size = 5
seed(1)
front = None
side = None


def north():
    print("north")


def south():
    print("south")


def east():
    print("east")


def west():
    print("west")


def stop():
    print("stop")


def northeast():
    print("northeast")


def northwest():
    print("northwest")


def southeast():
    print("southeast")


def southwest():
    print("southwest")


while True:
    new_x = randint(0, 10)
    new_size = randint(0, 10)
    print("Old x: " + str(old_x) + "|New x: " + str(new_x))
    print("Old size: " + str(old_size) + "|New size: " + str(new_size))

    front = new_size - old_size
    side = new_x - old_x
    print("Front: " + str(front) + " |Side: " + str(side))

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
