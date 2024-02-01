class Queue:
    def __init__(self):
        self.mylist= []

    def is_empty(self):
        return len(self.mylist)==0

    def enqueue(self,data):
        self.mylist.append(data)

    def dequeue(self):
        if not self.is_empty():
         self.mylist.pop(0)

    def get_front(self):
      if not self.is_empty():
          return self.mylist[0]
      else:
          raise IndexError("Queue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise IndexError("Queue is empty")



q = Queue()
#q.is_empty()
#q.enqueue(4)
#q.enqueue(7)
#print("dequeue element of a queue is ",q.dequeue())
#q.enqueue(79)
#print("Top element of a queue is ",q.get_front())
#print("Rear element of a queue is ",q.get_rear())
