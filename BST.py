class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    def insert(self,data):
     self.root = self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left,data)
        elif data > root.item:
            root.right = self.rinsert(root.right,data)
        return root

    def search(self,data):

     return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item == data:
            return root
        if data < root.item:
          return  self.rsearch(root.left,data)
        if data > root.item:
            return self.rsearch(root.right,data)

    def inOrder(self):
        result = []
        return self.rinorder(self.root,result)
    def rinorder(self,root,result):
     if root is not None:
        self.rinorder(root.left,result)
        result.append(root.item)
        self.rinorder(root.right, result)
        return result

    def preOrder(self):
        result = []
        return self.rpreorder(self.root,result)
    def rpreorder(self,root,result):
     if root is not None:
        result.append(root.item)
        self.rpreorder(root.left,result)
        self.rpreorder(root.right, result)
        return result


    def postOrder(self):
        result = []
        return self.rpostorder(self.root, result)
    def rpostorder(self, root, result):
      if root is not None:
          self.rpostorder(root.left, result)
          self.rpostorder(root.right, result)
          result.append(root.item)
          return result


    def max_value(self,temp):
        current = temp
        while(current!=None):
           current = current.right
        return current.item

    def min_value(self, temp):
        current = temp
        while (current != None):
            current = current.left
        return current.item


    def delete(self,data):
       self.root= self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        if data < root.item:
           root.left = self.rdelete(root.left,data)
        elif data > root.item:
            root.right = self.rdelete(root.right,data)
        else:
          if root.left is None:
           return root.right
          elif root.right is None:
            return root.left
          else:
             root.item = self.min_value(root.right) #successor logic
             self.rdelete(root.right, root.item)
        return root
            # root.item = self.max_value(root.left) #predecessor logic
            # self.rdelete(root.left,root.item)

    def size_of_tree(self):
     return len(self.inOrder())

bst = BST()
bst.insert(45)
bst.insert(70)
bst.insert(66)
bst.insert(80)
if bst.search(60):
  print("ROOT found")
else:
  print("ROOT not found")
  result_list = bst.inOrder()
print("Inorder Traversal ",result_list)

result_list = bst.preOrder()
print("Pre Order Traversel ",result_list)

result_list = bst.postOrder()
print("Post order Traversal ",result_list)

bst.delete(66)

result_list = bst.inOrder()
print("Inorder Traversal ",result_list)


print("The size of tree is ",bst.size_of_tree())