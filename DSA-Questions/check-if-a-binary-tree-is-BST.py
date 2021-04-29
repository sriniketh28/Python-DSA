class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

temp_arr = []
def inorder(root):
    if root:
        inorder(root.left)
        temp_arr.append(root.data)
        inorder(root.right)

def isBST(root):
    inorder(root)
    if temp_arr == sorted(temp_arr):
        print("BST")
    else:
        print("Not BST")

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

isBST(root)

