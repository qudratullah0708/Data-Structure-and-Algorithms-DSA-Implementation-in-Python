class Queue(list):
    def is_empty(self):
        return len(self)==0

    def enqueue(self,data):
        self.append(data)
    def dequeue(self):
     if not self.is_empty():
        super().pop(0)
     else:
         raise IndexError("Queue is empty")
    def get_front(self):
     if not self.is_empty():
        return self[0]
     else:
         raise IndexError("Queue is empty")
    def get_rear(self):
     if not self.is_empty():
        return self[-1]
     else:
         raise IndexError("Queue is empty")
    def get_size(self):
        return len(self)
    def insert(self, index, object):
        raise AttributeError("No insert attribute in Queue")
    def remove(self,index):
        raise AttributeError("No remove attribute in Queue")





q = Queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(9)
q.dequeue()
print("The queue is Empty: ",q.is_empty())
q.enqueue(78)
print("The rear element of a queue is ",q.get_rear() )
print("The front element of a queue is ",q.get_front())
print("The size of a queue is ",q.get_size())
try:
 q.remove(3)
except AttributeError as e:
    print(f"Caught an exception:{e}")

try:
 q.insert(4,5)
except AttributeError as e:
    print(f"Caught an exception:{e}")