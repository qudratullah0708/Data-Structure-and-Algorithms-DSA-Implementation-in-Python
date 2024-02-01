class node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self,start=None):
        self.start = start

    def isEmpty(self):
        return self.start is None
    def insert_at_first(self,data):
        n = node(data)
        n.next = self.start
        self.start = n

    def insert_at_last(self,data):
       if self.start is None:
            n = node(data)
            self.start = n
       else:
           temp = self.start
           while temp.next is not None:
            temp = temp.next
           n = node(data)
           temp.next = n

    def del_first(self):
        if self.start == None:
            print("No element in the list")
        elif self.start.next == None:
            self.start = None
        else:
            self.start = self.start.next

    def del_last(self):
        if self.start == None:
            print("No Element in the list")
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
               return temp
            temp = temp.next
        return None

    def insert_after(self,temp,data):
       if temp is not None:
           n = node(data,temp.next)
           temp.next = n



  #  def del_Item(self,data):
       # temp = self.start
      #  while temp is not None:
           # if




    def print_All(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next



s = SLL()
#s.isEmpty()
#s.insert_at_first(10)
#s.insert_at_last(20)
#s.insert_at_last(30)
#print(s.search(20))
#s.print_All()
#s.del_first()
#s.del_last()
#s.insert_after(s.search(30),25)
#print()
#s.print_All()