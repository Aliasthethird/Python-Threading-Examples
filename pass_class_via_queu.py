import queue

q = queue.Queue()

class Message(object):
    def __init__(self, key = 'Test', priority = 10):
        self.key = key
        self.priority = priority
    def foo(self):
        for i in range(self.priority):
            print(i, end = "-")
        print()

message_s = Message()
q.put(message_s)

message_s = Message("Test2", 5)
q.put(message_s)


message_s.key = "test3" # updats object in queue -> passed by reference?!
message_s.priority = 3
# q.put(message_s)

message_r = q.get(timeout=1)
print(message_r.key)
message_r.foo()

message_r = q.get(timeout=1)
print(message_r.key)
message_r.foo()

try:
    message_r = q.get(timeout=1)
    print(message_r.key)
    message_r.foo()
except:
    pass
