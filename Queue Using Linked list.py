class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self,front=None,rear=None):
        self.item_count = 0
        self.front = front
        self.rear = rear

    def is_empty(self):
        return self.front == None

    def enqueue(self,data):
       n = Node(data)
       if self.is_empty():
        self.front=n
        self.rear=n
       else:
         self.rear.next = n
         self.rear = n
       self.item_count+=1

    def dequeue(self):
        if not self.is_empty():
           if self.front.next is not None:
               data = self.front.item
               self.front = self.front.next
               return data
           else:
             data = self.front.item
             self.front = None
             self.rear = None
             return data
        else:
             raise IndexError("Queue underflow")
        self.item_count-=1

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue underflow")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue is empty")

    def size_of_queue(self):
        if not self.is_empty():
            return self.item_count
        else:
            raise IndexError("Queue underflow")


q = Queue()
q.is_empty()
q.enqueue(45)
q.enqueue(89)
print("Size of Queue: ",q.size_of_queue())

print("Removed element from the queue is ",q.dequeue())
q.enqueue(22)
q.enqueue(77)
print("Size of Queue: ",q.size_of_queue())
