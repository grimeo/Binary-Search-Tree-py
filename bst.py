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
                self.right.add_child(data)
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
   
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    myname = ['R', 'O', 'M', 'E', 'O', 'G', 'E', 'S', 'C', 'O', 'L', 'A', 'N', 'O']
    myname_tree = build_tree(myname)

    print("My name in elements",myname)

    print("In order : ", myname_tree.to_order_traversal())
    print("Pre order: ",myname_tree.to_pre_order_traversal())
    print("Post order : ",myname_tree.to_post_order_traversal())