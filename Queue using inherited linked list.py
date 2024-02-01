from SingleLinkedList import *

class Queue(SLL):
    def __init__(self):
        # We have to call the init method (constructor) of a parent class explicitly in python unlike c++ or jave
        super().__init__()
        self.item_count=0

    def is_empty(self):
        return self.isEmpty()
    def enqueue(self,data):
        self.insert_at_last(data)
        self.item_count+=1

    def dequeue(self):
      if not self.isEmpty():
        data = self.start.item
        self.del_first()
        self.item_count-=1
        return data
      else:
          print("linked list is already empty")

    def get_front(self):
        if not self.isEmpty():
           return self.start.item
        else:
            print("Linked list is empty")

    def get_rear(self):
        if not self.isEmpty():
            temp = self.start
            while temp.next!=None:
                temp=temp.next
            return temp.item

    def get_size(self):
        return self.item_count

q = Queue()
print("is the queue empty: ",q.is_empty())
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
print("is the queue empty: ",q.is_empty())
print("The removed element from the queue is ",q.dequeue())
print("The front element on a queue is : ",q.get_front())
print("The last element on a queue is : ",q.get_rear())
q.enqueue(33)
q.enqueue(99)
print("The front element on a queue is : ",q.get_front())
print("The last element on a queue is : ",q.get_rear())
print("The size of a queue is : ",q.get_size())


