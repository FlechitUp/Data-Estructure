import os

class node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class myTree():
    def __init__(self):
        self.root = None
        
    def insert(self, a, value):
        if a == None:
            a = node(value)
        else:
            d = a.value
            if value < d:
                a.left = self.insert(a.left, value)
            else:
                a.right = self.insert(a.right, value)
        return a
    
    
    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.value)
            self.preorder(a.left)
            self.preorder(a.right)
    
    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.value)
            self.inorder(a.right)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.value)

    def search(self, value, a):
        if a == None:
            return None
        else:
            if value == a.value:
                return a.value
            else:
                if value < a.value:
                    return self.search(value, a.left)
                else:
                    return self.search(value, a.right)
   
   
tree = myTree()
if __name__ == "__main__":

    while True:        
        opc = input("\n1.-Input node \n2.-Inorder \n3.-Preorder \n4.-Out\n\nChose an option -> ")

        if opc == '1':
            nodo = input('Input the node -> ')
            if nodo.isdigit():
                nodo = int(nodo)
                tree.root = tree.insert(tree.root, nodo)
            else:
                print('Only integers')
        elif opc == '2':
            if tree.root == None:
                print("----")
            else:
                tree.inorder(tree.root)
        elif opc == '3':
            if tree.root == None:
                print("----")
            else:
                tree.preorder(tree.root)
        elif opc == '4':            
            print('Bye')
            os.system("pause")
            break
        else:
            print('Bad option')
        print()
        os.system("pause")

    print() 
