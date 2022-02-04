import time
import threading
import queue


class Receiver(threading.Thread):
    """
    Receives from a Sender and returns a  sequential number to the sender.
    The Sender is given the Receiver object  as an input parameter
    """
    def __init__(self):
        self.in_q = queue.Queue()
        threading.Thread.__init__(self, daemon=True)
        self.start()

    def run(self): 
        i = 0
        while True:  
            incoming = self.in_q.get()
            print("new request from", incoming.sender_name, "answered with", i )   
            incoming.return_q.put(i)
            i += 1   

class Sender(threading.Thread):
    """
    Sends a request to a Receiver object and receives back a number
    indicating that this was the nth request to the Receiver
    """
    def __init__(self, name: str, receiver: Receiver, target=None):
        self.sender_name = name
        self.receiver = receiver
        self.return_q = queue.Queue()
        threading.Thread.__init__(self, daemon=False)
        self.start()

    def run(self): 
        for i in range(3):
            self.receiver.in_q.put(self)
            print(self.sender_name, 'received', self.return_q.get())
            time.sleep(1)

if __name__ == "__main__":
    receiver = Receiver()
    Sender("sender_1", receiver)
    Sender("sender_2", receiver)
    Sender("sender_3", receiver)