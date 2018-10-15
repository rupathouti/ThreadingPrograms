import thread;
import threading;
import time;

def Work(name,delay):
   count = 0;
   while count < 5:
       time.sleep(delay);
       count += 1;
       print("{} {}".format(name,count));


class Thread1 (threading.Thread):
   def __init__(self,name,delay):
       threading.Thread.__init__(self);
       self.name = name;
       self.delay = delay;

   def run(self):
       Work(self.name,self.delay)

def Main():
   print("Entering Main")
   i = 0
   while i < 10:
       print("Loop 1")
       i += 1
   t1 = Thread1("Amit",0.6)
   t1.start();
   thread.start_new_thread(Work,("Rahul",0.5))
   thread.start_new_thread(Work,("Jagrat",0.2))
   i = 0
   while i < 10:
       print("Main")
       time.sleep(0.5)
       i += 1
   print("Leaving Main")

Main()
