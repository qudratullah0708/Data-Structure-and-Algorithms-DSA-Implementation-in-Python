class priortyQueue:
    def __init__(self):
        self.items = []

    def push(self,data,priority_no):
        index = 0
        #The indexing [1] is used to access the second element of the tuple, which is the priority number.
        while index<len(self.items)  and self.items[index][1]<=priority_no:
            index+=1
        self.items.insert(index,(data,priority_no))

    def is_empty(self):
       return len(self.items)==0

    def pop(self):
        if not self.is_empty():
          return  self.items.pop(0)[0]
        else:
            raise IndexError("Priority Queue is empty")
    def size(self):
        return self.len(self.items)


pq = priortyQueue()
pq.push(4543,5)
pq.push(573,9)
pq.push(75483,8)
pq.push(545432,1)
while not pq.is_empty():
    print(pq.pop())