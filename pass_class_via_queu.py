import queue
from copy import deepcopy

q = queue.Queue()

class Message(object):
    def __init__(self, key = 'Default', priority = 10):
        self.key = key
        self.priority = priority
    def foo(self):
        for i in range(1,self.priority+1):
            print(i, end = " ")
        print()

message_s = Message()
q.put(message_s)

message_s = Message("Test 1", 5) # New object in queue
q.put(message_s)

message_s = Message("Test 2", 5)
q.put(message_s)

message_s.key = "override Test 2" # updats object in queue -> passed by reference?!
message_s.priority = 3
q.put(message_s)

message_s = Message("Test 3", 5)
q.put(deepcopy(message_s))

message_s.key = "dose not override Test 3" # updats object in queue -> passed by reference?!
message_s.priority = 3
q.put(message_s)


for i in range(7):
    try:
        message_r = q.get(timeout=1)
        print('key = ', message_r.key)
        message_r.foo()
    except:
        print('timeout')

