import time
import threading
import queue

class Request():
    """
    Containr to pass message to Receiver via return queue
    """
    def __init__(self, q: queue.Queue):
        self.q = q

    def set_request(self, request: str):
        self.request = request

    def get_request(self) -> str:
        return self.request

    def put(self, return_value: str):
        self.q.put(return_value)

class Receiver(threading.Thread):
    """
    Receives from a Sender and returns a  sequential number to the sender.
    The Sender is given the Receiver object  as an input parameter
    """
    def __init__(self):
        self._in_q = queue.Queue()
        threading.Thread.__init__(self, daemon=True)
        self.start()

    def run(self): 
        i = 0
        while True:  
            incoming = self._in_q.get()
            print("new request from", incoming.get_request(), "answered with", i )   
            incoming.put(i)
            i += 1   

    def put(self, return_message) -> None:
        self._in_q.put(return_message)


class Sender(threading.Thread):
    """
    Sends a request to a Receiver object and receives back a number
    indicating that this was the nth request to the Receiver
    """
    def __init__(self, name: str, receiver: Receiver):
        
        self.sender_name = name
        self.receiver = receiver
        self.return_q = queue.Queue()
        self.request = Request(self.return_q)
        self.request.set_request(self.sender_name)
        threading.Thread.__init__(self, daemon=False)
        self.start()

    def run(self): 
        for i in range(3):
            self.receiver.put(self.request)
            print(self.sender_name, 'received', self.return_q.get())
            time.sleep(1)

if __name__ == "__main__":
    receiver = Receiver()
    Sender("sender_1", receiver)
    Sender("sender_2", receiver)
    Sender("sender_3", receiver)