class deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def insert_at_front(self,data):
        self.items.insert(0,data)
    def insert_at_rear(self,data):
        self.items.append(data)
    def del_first(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Deque is empty")
    def del_rear(self):
        if not self.is_empty():
            return self.items.pop(-1)
        else:
            raise IndexError("deque is empty")

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("deque is empty")

    def get_rear(self):
      if not self.is_empty():
        return self.items[-1]
      else:
        raise IndexError("deque is empty")
    def size_deque(self):
        return len(self.items)

d = deque()
d.insert_at_front(45)
d.insert_at_rear(56)
try:
 d.del_first()
except IndexError as e:
 print(f"Caught an exception as {e}")
d.insert_at_front(77)
try:
 d.del_rear()
except IndexError as e:
    print(f"Caught an exception error as {e}")
print("The size of deque is ",d.size_deque())