class Tree():
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
    def inordersuccessor(self):
        current = self
        while current.leftchild != None:
            current = current.leftchild
        return current
    def inorder(self): 
        #left root right
        if self.leftchild != None:
            self.leftchild.inorder()
        print(self.data)
        if self.rightchild != None:
            self.rightchild.inorder()
    def preorder(self):
        #Root left right
        print(self.data)
        if self.leftchild != None:
            self.leftchild.preorder()
        if self.rightchild != None:
            self.rightchild.preorder()
    def postorder(self):
        #left right root
        if self.leftchild != None:
            self.leftchild.postorder()
        if self.rightchild != None:
            self.rightchild.postorder()
        print(self.data)
    def search(self,value):
        if self.data == value:
            return self
        elif value > self.data and self.rightchild != None:
            return self.rightchild.search(value)
        elif value < self.data and self.leftchild != None:
            return self.leftchild.search(value)
        else:
            return False
    def insert(self,addedvalue):
        if self == None: 
           return Tree(addedvalue)
        if addedvalue < self.data:
           self.leftchild = self.leftchild.insert(addedvalue)
        elif addedvalue > self.data:
           self.rightchild = self.rightchild.insert(addedvalue)
        return self
    def delete(self,deletevalue):
        if self == None:
            return self
        if deletevalue < self.data:
            self.leftchild = self.leftchild.delete(deletevalue)
        elif deletevalue > self.data:
            self.rightchild = self.rightchild.delete(deletevalue)
        else:
            #root has only one child
            if self.leftchild == None:
                temp = self.rightchild
                self = None
                return temp
            elif self.rightchild == None:
                temp = self.leftchild
                self = None
                return temp
            #root has 2 children
            else:
                temp = self.inordersuccessor()
                t = self.data
                self.data = temp.data
                temp.data = t
                self.rightchild = self.rightchild.delete(temp.data)
        return self
    


objectone = Tree(50)
objectone.leftchild = Tree(30)
objectone.rightchild = Tree(90)
objectone.leftchild.leftchild = Tree(20)
objectone.leftchild.leftchild.leftchild = Tree(10)
objectone.leftchild.rightchild = Tree(40)
objectone.rightchild.rightchild = Tree(100)
print("inorder")
objectone.inorder()
print("preorder")
objectone.preorder()
print("postorder")
objectone.postorder()


searchelement = int(input("Which number do you want to search for? "))
result = objectone.search(searchelement)
if result == False:
    print("Number was not found")
else:
    print("Number is present")

#insertelement = int(input("Which number do you want to insert? "))
#objectone.insert(insertelement)
objectone.inorder()
delitem = int(input("Which number do you want to delete? "))
objectone.delete(delitem)
objectone.inorder()
