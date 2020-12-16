#!/usr/bin/env/python3

import OPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setmode(GPIO.BCM)

GPIO.setup(9,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

global count
global counting

counting = 0

def firstFunction():
        global counter
        global ts
        global counting
        count = 1
        counter = 0
        ts = time.time()
        while True:
                if (count == 1):
                        GPIO.wait_for_edge(27, GPIO.RISING)
                        counting = 1
                        counter += 1
                        print("Pulse comming ! (%s)") % counter
                        ts = time.time()


def secondFunction():
        global count
        global counting
        global counter
        while True:
                cts = ts + 2
                if (cts < time.time()):
                        print("Counting looks like finished with %s pulses") % counter
                        count = 0
                        counting = 0
                        print("We process the Payment NOW !")

                        if (counter == 1):
                                print('Piso')
                        if (counter == 2):
                                print('Lima')
                        if (counter == 3):
                                print('Sampu')
                                
                        counter = 0
                        count = 1
                        print("Ready to process the next payment !")
                time.sleep(1)


def thirdFunction():
        while True:
                if (counting == 0):
                        global ts
                        ts = time.time()
                        time.sleep(1)



try:
        t1 = Thread(target = firstFunction)
        t2 = Thread(target = secondFunction)
        t3 = Thread(target = thirdFunction)

        t1.start()
        t2.start()
        t3.start()

except KeyboardInterrupt:
        t1.stop()
        t2.stop()
        t3.stop()
        GPIO.cleanup()
