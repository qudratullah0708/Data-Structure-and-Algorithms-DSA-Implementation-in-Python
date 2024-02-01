class node:
   def __init__(self,prev=None,item=None,next=None):
       self.prev = prev
       self.item = item
       self.next = next


class CDLL:
   def __init__(self, start = None):
        self.start = start


   def is_empty(self):
       if self.start is None:
           print("Linked list is empty")
       else:
           print("Linked list is not empty")
   def insert_at_first(self,data):
     n = node(item=data)
     if self.start is None:
           n.next = n
           n.prev = n
     else:
           n.next = self.start
           n.prev = self.start.prev
           self.start.prev.next=n
           self.start.prev=n
     self.start=n

   def insert_at_last(self,data):
       n = node(item=data)
       if self.start is None:
           n.next = n
           n.prev = n
           self.start=n
       else:
           n.next = self.start
           n.prev = self.start.prev
           self.start.prev.next=n
           self.start.prev = n

   def insert_after(self,temp,data):
       if temp is not None:
           n = node(item=data)
           n.prev=temp
           n.prev=temp
           n.next = temp.next
           temp.next = n
           temp.next.prev = n

   def search(self,data):
       temp = self.start
       if temp ==None:
           return None
       if temp.item == data:
           return temp

       else:
           temp = temp.next
           while temp != self.start:
               if temp.item == data:
                   return temp
               temp = temp.next
           return None

   def print_all(self):
       temp = self.start
       if temp is not None:
           print(temp.item, end=" ")
       temp = temp.next
       while temp != self.start:
           print(temp.item, end=" ")
           temp = temp.next


   def del_first(self):
       if self.start is not None:
           if self.start.next==self.start:
               self.start=None
           else:
               self.start.prev.next=self.start.next
               self.start.next.prev=self.start.prev
               self.start=self.start.next

   def del_last(self):
       if self.start is not None:
           if self.start.next == self.start:
               self.start=None
           else:
               self.start.prev.prev.next = self.start
               self.start.prev = self.start.prev.prev

   def del_item(self,data):
       if self.start is not None:
           if self.start.next == self.start:
             if self.start.item==data:
               self.start=None
             else:
               temp = self.start
               temp = temp.next
               while temp!=self.start:
                   if temp.item==data:
                       temp.prev.next=temp.next
                       temp.next.prev=temp.prev
                   temp=temp.next







