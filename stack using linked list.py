class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class stack:
    def __init__(self,top=None,count=0):
        self.top = top
        self.count = count

    def is_empty(self):
        return self.top==None

    def push(self,data):
        n = Node(data)
        n.next = self.top
        self.top=n
        self.count+=1
    def pop(self):
         if not self.is_empty():
             data = self.top.item
             if self.top.next is not None:
                 self.top = self.top.next
             else:
                 self.top = None
             self.count-=1
             return data
         else:
             raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top.item
        else:
            raise IndexError("Stack is empty")

    def size_of_stack(self):
        print("Size of stack is ",self.count)


s1 = stack()
s1.push(45)
s1.push(323)
s1.size_of_stack()
print("The top element on the stack is ",s1.peek())
print("The pop element from the stack is",s1.pop())
s1.size_of_stack()



