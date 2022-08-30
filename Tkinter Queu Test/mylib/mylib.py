import queue
import threading
import time

class Receiver(threading.Thread):
    """
    Receives from a Sender
    """
    def __init__(self):
        self._in_q = queue.Queue()
        threading.Thread.__init__(self, daemon=True)
        self.start()

    def run(self): 
        i = 0
        t_start = time.monotonic()
        while True:  
            t0 = time.monotonic()
            try:
                incoming = self._in_q.get(timeout = 1)
            except queue.Empty:
                print(f"time elapsed: {time.monotonic() - t0}")
                print("q empty")
            else:
                print(f"time elapsed: {time.monotonic() - t0}")
                print(incoming)

            print(f"time elapsed = {time.monotonic() - t_start} s")


    def put(self, message) -> None:
        self._in_q.put(message)