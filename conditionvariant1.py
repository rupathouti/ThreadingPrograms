#Here we are using CONDITION i.e. Monitors in other languages...To solve the problem of shared resources we use condition...In multi threading, only one thread can use the variables at one time, another threads need to wait for the resource to become wakened...Locking of all threads accept one is known as Condition or Monitor...

from threading import *
import time

lapMoniter = Condition()


class TestBed:
    def busyTracks(self):
        lapMoniter.acquire()
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
        lapMoniter.release()

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
