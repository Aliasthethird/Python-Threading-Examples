import queue

q = queue.Queue()

class Message:
    def __init__(self, key = 'Test', priority = 0):
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

# message_s.key = "test3" 
# message_s.priority = 1
# q.put(message_s)

message_r = q.get()
print(message_r.key)
message_r.foo()

message_r = q.get()
print(message_r.key)
message_r.foo()

message_r = q.get()
print(message_r.key)
message_r.foo()
