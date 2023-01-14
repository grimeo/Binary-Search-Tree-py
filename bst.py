class BinarySearchTreeNode:
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
                self.left = BinarySearchTreeNode(data)
        else: 
            if self.right:
                self.right.add_add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
        
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def to_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.to_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.to_order_traversal()
        return elements
    
    def to_post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.to_post_order_traversal()
        if self.right:
            elements += self.right.to_post_order_traversal()
        elements.append(self.data)
        return elements
    
    def to_pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.to_pre_order_traversal()
        if self.right:
            elements += self.right.to_pre_order_traversal()
            return elements
   