class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None


    def insert(self,d):
        if self.value == d:
            return False
        elif d<self.value:
            if self.left != None:
               return self.left.insert(d)
            else: 
                self.left=Node(d)
                return True
        else:
            if self.right != None:
                return self.right.insert(d)
            else: 
                self.right = Node(d)
                return True  

    def find(self,d):
        if d<self.value and self.left!=None:
            return self.left.find(d)
        elif d>self.value and self.right!=None:
            return self.right.find(d)
        elif self.value==d:
            return True
        else: 
            return False

    def preOrderPrint(self):
        print(self.value)
        if self.left !=None:
            self.left.preOrderPrint()
        if self.right !=None:
            self.right.preOrderPrint()
    
    def inOrderPrint(self):
        if self.left !=None:
            self.left.inOrderPrint()
        print(self.value)
        if self.right !=None:
            self.right.inOrderPrint()

    def revInOrder(self,level):
        if self.right !=None:
            self.right.revInOrder(level+3)
        for i in range(level): 
            print(end = " ")
        print(self.value)
        print()
        if self.left!=None: 
            self.left.revInOrder(level+3)

    
    def postOrderPrint(self):
        if self.left !=None:
            self.left.postOrderPrint()
        if self.right !=None:
            self.right.postOrderPrint()
        print(self.value)

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self,d):
        if self.root != None:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True
    
    def find(self,d):
        if self.root !=None:
            return self.root.find(d)
        else: 
            return False
    
    def preOrderPrint(self):
        if self.root !=None:
            return self.root.preOrderPrint()
        else:
            return 
    
    def inOrderPrint(self):
        if self.root !=None:
            return self.root.inOrderPrint()
        else:
            return

    def revInOrder(self,l):
        if self.root != None:
            return self.root.revInOrder(l)
        else:
            return

    def postOrderPrint(self):
        if self.root != None: 
            return self.root.postOrderPrint()
        else:
            return

    def delete(self,d):
        #1 tómt tré
        if self.root == None:
            return False
        #2 drepa rót
        #2.1 rótin á engin börn
        if self.root.value == d:
            if self.root.left == None and self.root.right == None:
                self.root = None
                return True
            #2.2: rótin á barn vinstra megin
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
                return True
            # 2.3:rótin á barn hægra megin
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
                return True
            # 2.4: rótin á börn báðum megin
            else:
                moveNode = self.root.right
                moveNodeParent = self.root
                while moveNode.left:
                    moveNodeParent = moveNode
                    moveNode = moveNode.left
                self.root.value = moveNode.value
                if moveNode.value < moveNodeParent.value:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
                return True     
        # Finna hnútinn sem á að drepa
        parent = None
        node = self.root
        while node and node.value != d:
          parent = node
          if d < node.value:
            node = node.left
          elif d > node.value:
            node = node.right
        # 3: hnúturinn finnst ekki
        if node == None or node.value != d:
          return False
        # 4: hnúturinn er ekki með nein börn
        elif node.left is None and node.right is None:
          if d < parent.value:
            parent.left = None
          else:
            parent.right = None
          return True
        # 5: hnúturinn er með vinstra barn
        elif node.left and node.right is None:
          if d < parent.value:
            parent.left = node.left
          else:
            parent.right = node.left
          return True
        # 6: hnúturinn er bara með hægra barn
        elif node.left is None and node.right:
          if d < parent.value:
            parent.left = node.right
          else:
            parent.right = node.right
          return True
        # 7: hnúturinn er með vinsta og hægra barn, aðeins meiri flækja
        else:
            moveNodeParent = node
            moveNode = node.right
            while moveNode.left:
                moveNodeParent = moveNode
                moveNode = moveNode.left
            node.value = moveNode.value
            if moveNode.right:
                if moveNode.value < moveNodeParent.value:
                    moveNodeParent.left = moveNode.right
                else:
                    moveNodeParent.right = moveNode.right
            else:
                if moveNode.value < moveNodeParent.value:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
            return True


# Tímamælir
import time

    

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        self._start_time = time.perf_counter()

    def stop(self):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Liðin tími: {elapsed_time:0.4f} sekúndur")


t = Tree()
t.insert(20)
t.insert(10)
t.insert(5)
t.insert(15)
t.insert(17)
t.insert(30)
t.insert(25)
t.insert(35)
print()
t.delete(20)
t.inOrderPrint()
print()
print(t.find(1))
print(t.find(35))
t.postOrderPrint()
t.delete(17)
print()
t.revInOrder(0)

print()


L = [i for i in range(2000,0,-1)]
print(L)

k=Timer()

k.start()
r=Tree()
for i in L:
    r.insert(i)

r.inOrderPrint()
k.stop()