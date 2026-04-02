class Tree():
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
    def inorder(self): 
        #left root right
        if self.leftchild != None:
            self.leftchild.inorder()
        print(self.data)
        if self.rightchild != None:
            self.rightchild.inorder()
        


objectone = Tree(2)
objectone.leftchild = Tree(1)
objectone.rightchild = Tree(0)
objectone.leftchild.leftchild = Tree(3)
objectone.leftchild.rightchild = Tree(4)
objectone.rightchild.leftchild = Tree(5)
objectone.rightchild.rightchild = Tree(6)
objectone.inorder()



#write for preorder (Root, Left, Right)
#write for postorder (Left, Right, Root)
