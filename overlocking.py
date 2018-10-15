from threading import *
import time

lapMoniter = Condition()

class RacingCircuit:

    def __init__(self):
        self.lap = 0


    def busyTracks(self):
        with lapMoniter:
            t = current_thread()
            print("{} Entered Busy Tracks".format(t.name))
            while(self.lap < 5):
                if(t.name == "Car"): print("brrrommsss")
                else: print("vrrrommsss")
                time.sleep(1)
                self.lap += 1
                print("Lap = {}".format(self.lap))
            self.lap = 0
            print("{} Leaving Busy Tracks".format(t.name))

    def busyLanes(self):
        with lapMoniter:
            t = current_thread()
            print("{} Entered Busy Lanes".format(t.name))
            while(self.lap < 5):
                if(t.name == "Car"): print("brrrommsss")
                else: print("vrrrommsss")
                time.sleep(1)
                self.lap += 1
                print("Lap = {}".format(self.lap))
            self.lap = 0
            print("{} Leaving Busy Tracks".format(t.name))

a = RacingCircuit()
b = RacingCircuit()


class Bike(Thread):
    def __init__(self):
        Thread.__init__(self,name="Bike")

    def run(self):
        print("Bike Starts Journey")
        global a
        a.busyTracks()
        a.busyLanes()
        a.busyLanes()
        print("Bike Ends Journey")


class Car(Thread):
    def __init__(self):
        Thread.__init__(self,name="Car")

    def run(self):
        print("Car Starts Journey")
        global b
        b.busyLanes()
        b.busyTracks()
        b.busyLanes()
        print("Car Ends Journey")

Car().start()

Bike().start()
