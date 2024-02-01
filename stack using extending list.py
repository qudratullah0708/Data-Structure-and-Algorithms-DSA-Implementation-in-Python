class stack(list):
   def is_empty(self):
     return len(self)==0
   def pop(self):
       if not self.is_empty():
        return super().pop()
       else:
         raise IndexError("Stack is empty")
   def push(self,data):
       self.append(data)
   def peek(self):
       if not self.is_empty():
        return self[-1]
       else:
           raise IndexError("Stack is empty")
   def insert(self,index,data):
       raise AttributeError("No Attribute insert in stack")

   def sizeof_stack(self):
       return len(self)

s1 = stack()
s1.push(4)
print("The pop element from the stack is ",s1.pop())
s1.insert(3,5)