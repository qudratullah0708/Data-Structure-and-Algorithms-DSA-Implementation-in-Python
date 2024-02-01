from SingleLinkedList import *
class stack(SLL):
     def __init__(self):
#We have to call the init method (constructor) of a parent class explicitly in python unlike c++ or jave
         super().__init__()
         self.item_count = 0
     def is_empty(self):
         return self.isEmpty()
     def push(self,data):
         self.insert_at_first(data)
         self.item_count+=1
     def pop(self):
         if not self.is_empty():
             data = self.start.item
             self.item_count -= 1
             return  data

         else:
             raise IndexError("Stack underflow")
     def peek(self):
       if not self.is_empty():
         return self.start.item
       else:
           raise IndexError("Stack under flow")

     def size_of_stack(self):
         return self.item_count

     def insert_after(self,temp,data):
         raise AttributeError("No insert after attribute available in the stack")
     def insert_at_last(self,data):
         raise AttributeError("No insert at last attribute available in stack")



s = stack()
s.push(5)
print("The poped element is ",s.pop())
s.push(6)
print("The top element of the stack is ",s.peek())
print("The size of a stack is ",s.size_of_stack())
