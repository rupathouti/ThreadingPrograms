from threading import *
#Import everything from module threading
import time

class TestBed:
    def busyTracks(self):
        t = current_thread()
        print("{} Entered Busy Tracks".format(t.name))
        lap = 0
        while(lap < 5):
            if(t.name == "Car"): print("brrrommsss")
            else: print("vrrrommsss")
            time.sleep(1)
            lap += 1
            print("Lap = {}".format(lap))
        lap = 0
        print("{} Leaving Busy Tracks".format(t.name))


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
