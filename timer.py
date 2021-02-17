#!/usr/bin/python3
import time
import sys

#create timer
class timer:
    #initialize timer
    def __init__(self):
        time_start = time.time()
        seconds = 0
        minutes = 0
        lava_level = 1

    def run(self):
        while True:
            sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
            sys.stdout.flush()
            time.sleep(1)
            seconds = int(time.time() - time_start) - minutes * 60
            if seconds >= 60:
                minutes += 1
                seconds = 0
            if seconds % 10 == 0:
                lava_level += 1
            print(lava_level)

