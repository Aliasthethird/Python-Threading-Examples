import queue

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

message_s = Message("Test1", 5) # New object in queue

message_s = Message("Test2", 5)
q.put(message_s)

message_s.key = "Overide Test2" # updats object in queue -> passed by reference?!
# message_s.priority = 3
q.put(message_s)

for i in range(5):
    try:
        message_r = q.get(timeout=1)
        print('key = ', message_r.key)
        message_r.foo()
    except:
        print('timeout')

