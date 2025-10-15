
from pyfirmata2 import Arduino, util
import time


board = Arduino(Arduino.AUTODETECT)
board.digital[9].mode = 1
board.digital[8].mode = 1


def green_light():
    board.digital[9].write(1)
    time.sleep(0.5)
    board.digital[9].write(0)
    time.sleep(0.5)
    board.digital[9].write(1)
    time.sleep(0.5)
    board.digital[9].write(0)
    time.sleep(0.5)
    board.digital[9].write(1)
    time.sleep(0.5)
    board.digital[9].write(0)
    time.sleep(0.5)


def red_light():
    board.digital[8].write(1)
    time.sleep(0.5)
    board.digital[8].write(0)
    time.sleep(0.5)
    board.digital[8].write(1)
    time.sleep(0.5)
    board.digital[8].write(0)
    time.sleep(0.5)
    board.digital[8].write(1)
    time.sleep(0.5)
    board.digital[8].write(0)
    time.sleep(0.5)
