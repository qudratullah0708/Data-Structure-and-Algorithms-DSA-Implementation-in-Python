class node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class deque:
    def __init__(self):
      self.start= None
      self.rear = None
      self.item_count=0

    def is_empty(self):
        return self.start==None

    def insert_at_first(self,data):
        n = node(data)
        if not self.is_empty():

            n.next=self.start
            n.prev=None
            self.start=n
        else:
            self.start=n
            self.rear=n
        self.start.prev=n
        self.item_count+=1

    def insert_at_rear(self,data):
     n = node(data)
     if not self.is_empty():
         n.prev = self.rear
         self.rear.next=n
     else:
         self.start = n
         self.rear = n
     self.item_count += 1

    def del_first(self):
          if not self.is_empty():
            if self.start.next!=None:
                self.start=self.start.next
                self.start.prev = None
            else:
              self.start=None
            self.item_count -= 1
          else:
              raise IndexError("Deque is empty")

    def del_rear(self):
         if not self.is_empty():
           if self.start==self.rear:
            self.start=None
            self.rear=None
           else:
               self.rear = self.rear.prev
               self.rear.next=None
           self.item_count -= 1
         else:
             raise IndexError("Deque is empty")


    def size_of_deque(self):
        return self.item_count


d = deque()
print(f"Size of deque is ",d.size_of_deque())
try:
 d.del_rear()
except IndexError as e:
    print(f"Caught exception error as {e}")
try:
    print("The deleted item from the deque is",d.del_first())
except IndexError as e:
    print(f"Caught exception error as {e}")

d.insert_at_first(56)
d.insert_at_rear(67)
print(f"Size of deque is ",d.size_of_deque())
d.insert_at_first(3)
d.is_empty()
d.insert_at_first(56)
d.insert_at_rear(67)
print(f"Size of deque is ",d.size_of_deque())
try:
    print("The deleted item from the deque is",d.del_first())
except IndexError as e:
    print(f"Caught exception error as {e}")
print(f"Size pf deque is ",d.size_of_deque())






