from SingleLinkedList import *
class stack:
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0
    def is_empty(self):
        return self.mylist.isEmpty()
    def push(self,data):
            self.mylist.insert_at_first(data)
            self.item_count+=1
    def pop(self):
        if not self.mylist.isEmpty():
            self.mylist.del_first()
            self.item_count-=1
    def peek(self):
        if not self.mylist.isEmpty():
            return self.mylist.start.item
        else:
            print("Stack is empty")
    def size_of_stack(self):
       print("Size of stack is ",self.item_count)


s1 = stack()
s1.push(45)
s1.push(4322)
s1.pop()
s1.push(4322)
print("Top element of stack is ",s1.peek())
s1.size_of_stack()