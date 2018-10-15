#One monitor can control the multiple blocks...we cannot define for all functions separately...

from threading import *
import time

lapMoniter = Condition()


class TestBed:
    def busyTracks(self):
        with lapMoniter:
            t = current_thread()
            print("{} Entered Busy Tracks".format(t.name))
            while(TestBed.lap < 5):
                if(t.name == "Car"): print("brrrommsss")
                else: print("vrrrommsss")
                time.sleep(1)
                TestBed.lap += 1
                print("Lap = {}".format(TestBed.lap))
            TestBed.lap = 0
            print("{} Leaving Busy Tracks".format(t.name))

    def busyLanes(self):
        with lapMoniter:
            t = current_thread()
            print("{} Entered Busy Lanes".format(t.name))
            while(TestBed.lap < 5):
                if(t.name == "Car"): print("brrrommsss")
                else: print("vrrrommsss")
                time.sleep(1)
                TestBed.lap += 1
                print("Lap = {}".format(TestBed.lap))
            TestBed.lap = 0
            print("{} Leaving Busy Tracks".format(t.name))


TestBed.lap = 0

class Bike(Thread):
    def __init__(self):
        Thread.__init__(self,name="Bike")

    def run(self):
        print("Bike Starts Journey")
        TestBed().busyLanes()
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
