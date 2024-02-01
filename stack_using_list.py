class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
         self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
      if not self.is_empty():
        return self.items[-1]
      else:
          raise IndexError("Stack is empty")
    def size_of_stack(self):
            return len(self.items)


s = stack()
s.is_empty()
s.push(45)
s.push(32)
#print("Removed element is ",s.pop())
s.push(100)
#print("Top Element is ",s.peek())
#print("Size of stack is ",s.size_of_stack())
