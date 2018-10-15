from threading import *
import time

class TestBed:
    def busyTracks(self):
        t = current_thread()
        print("{} Entered Busy Tracks".format(t.name))
        while(TestBed.lap < 5):
            if(t.name == "Car"): print("Bhaskar")
            else: print("Rupa")
            time.sleep(1)
            TestBed.lap += 1
            print("Lap = {}".format(TestBed.lap))
        TestBed.lap = 0
        #CLass is also a object so TestBed.lap
        print("{} Leaving Busy Tracks".format(t.name))

TestBed.lap = 0

class Bike(Thread):
    def __init__(self):
        Thread.__init__(self,name="Bike")

    def run(self):
        print("Bike Starts Journey")
        TestBed().busyTracks()
        print("Bike Ends Journey")


class Car(Thread):
    def __init__(self):
        Thread.__init__(self,name="Car")

    def run(self):
        print("Car Starts Journey")
        TestBed().busyTracks()
        print("Car Ends Journey")

Car().start()

Bike().start()
