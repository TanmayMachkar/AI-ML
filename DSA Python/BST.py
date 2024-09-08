class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)
                
    def inorder(self):
        elements = []
        
        if self.left:
            elements += self.left.inorder()
            
        elements.append(self.data)
        
        if self.right:
            elements += self.right.inorder()
            
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        
        if self.data > val:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if self.data < val:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_max(self):
        if self.rigth is None:
            return self.data
        self.right.find_max()
        
    def find_min(self):
        if self.left is None:
            return self.data
        self.left.find_min()
        
    def delete(self, val):
        if val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        elif val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
            
def build():
    root = BST(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root
    
if __name__ == '__main__':
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    elementsGet = build()
    elementsGet.delete(20)
    print(elementsGet.inorder())