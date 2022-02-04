"""
Demonstrates how to pass objects via a queue.


"""

__author__ = 'Gero Nootz'
__version__ = '1.0.0'
__email__ = 'gero.noozt@usm.edu'
__status__ = 'Prototype'

import queue
import copy 



class Message:
    def __init__(self, key = 'Default', priority = 10):
        self.key = key
        self.priority = priority
    def foo(self):
        for i in range(1,self.priority+1):
            print(i, end = " ")
        print()
        
q = queue.Queue()

def foo():
    message_s = Message()
    for i in range(2):
        q.put(message_s)

foo()

message_s = Message("Test 1", 5) # New object in queue
q.put(message_s)

message_s = Message("Test 2", 5)
q.put(message_s)

message_s.key = "override Test 2" # updats object in queue -> passed by reference?!
message_s.priority = 3
q.put(message_s)

message_s = Message("Test 3", 5)
q.put(copy.copy(message_s)) # deepcopy appears unnecessary here

message_s.key = "dose not override Test 3" 
message_s.priority = 3
q.put(message_s)


for i in range(q.qsize() + 1): # +1 to observe timeout behaviour
    try:
        message_r = q.get(timeout=1)
        print('key = ', message_r.key)
        message_r.foo()
    except:
        print('timeout')

