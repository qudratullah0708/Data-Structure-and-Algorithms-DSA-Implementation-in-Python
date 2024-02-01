class node:
    def __init__(self,item=None,priorty=None,next=None):
        self.item = item
        self.priorty=priorty
        self.next=next

class priortyQueue:
    def __init__(self):
        self.start=None
        self.item_count=0
    def is_empty(self):
        return self.start==None
    def push(self,data,priorty):
        n = node(data,priorty)
        if self.start==None or self.start.priorty<priorty:
            n.next=self.start
            self.start=n
        else:
            temp = self.start
            while temp.next!=None and temp.next.priorty<=priorty:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1

    def pop(self):
      if not self.item_count==0:
          data = self.start.item
          self.start=self.start.next
          return data
      else:
         raise IndexError("PriortyQueue is empty")

    def size(self):
         return self.item_count

pq = priortyQueue()
pq.push(4543,5)
pq.push(573,9)
pq.push(75483,8)
pq.push(545432,1)
while not pq.is_empty():
    print(pq.pop())