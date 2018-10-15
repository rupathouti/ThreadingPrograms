import socket
import threading
from TSQueue import TSQueue

print("Welcome to Concurrent Server 2.0")

queue = TSQueue()

clist = [];


class Conversation (threading.Thread):
    def __init__(self,soc):
        threading.Thread.__init__(self)
        self.soc = soc

    def run(self):
        global queue
        global clist
        clist.append(self.soc)
        msg = self.soc.recv(1024)
        msg = msg.decode()
        while msg != "q":
            queue.enqueue(msg)
            print(msg)
            msg = self.soc.recv(1024)
            msg = msg.decode()
        print("Client Disconnected")
        clist.remove(self.soc)
        self.soc.send("end".encode());
        self.soc.close()


class MessageDispatcher(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        pass

    def run(self):
        global queue
        global clist
        while True:
            message = queue.dequeue()
            [soc.send(message.encode()) for soc in clist]


ss = socket.socket()
hname = "localhost"
print("host name",hname)
port = 8091
ss.bind((hname,port))
ss.listen(5)
messagedispatcher = MessageDispatcher()
messagedispatcher.setDaemon(True)
messagedispatcher.start()
while True:
    c,addr = ss.accept()
    print("Connection Established with ",addr)
    Conversation(c).start()
ss.close()
print("Server Shutting Down")

class TSQueue:
    def __init__(self):
        self.q = [];
        self.monitor = threading.Condition();

    def enqueue(self,msg):
        with self.monitor:
            self.q.append(msg)
            self.monitor.notify()

    def dequeue(self):
        with self.monitor:
            if(self.isEmpty()):
                self.monitor.wait()
            msg = self.q[0]
            self.q.remove(self.q[0])
            return msg

    def isEmpty(self):
        return (len(self.q) == 0);
