class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def search(root, data):
    if root is None:
        return "Not present in BST"
    elif root.data == data:
        return str(root.data) + " is present in BST"
    elif root.data < data:
        return search(root.right, data)
    else:
        return search(root.left, data)

def insert(root, data):
    if root is None:
        return Node(data)
    elif root.data < data:
        root.right = insert(root.right, data)
    elif root.data > data:
        root.left = insert(root.left, data)
    return root

def maxNode(root):
    temp = root
    while(temp.right is not None):
        temp = temp.right
    return temp

def delete(root, data):
    if root is None:
        return None

    if root.data < data:
        root.right = delete(root.right, data)
    
    elif root.data > data:
        root.left = delete(root.left, data)

    else:
        if root.left is None and root.right is None:
            return None

        elif root.left and root.right:
            pre = maxNode(root.left)

            root.data = pre.data

            root.left = delete(root.left, pre.data)

        else:
            child = root.left if root.left else root.right
            root = child

    return root

def printLevelOrder(root):
    height = maxDepth(root)
    for i in range(1,height+2):
        printGivenLevel(root, i)

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    if level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def minValue(root):
    temp = root
    while(temp.left is not None):
        temp = temp.left
    print(temp.data)

def maxValue(root):
    temp = root
    while(temp.right is not None):
        temp = temp.right
    print(temp.data)

# maxDepth or height is same in a Tree

def maxDepth(root):
    if root is None:
        return -1
    else:
        lDepth = maxDepth(root.left)
        rDepth = maxDepth(root.right)

        return max(lDepth, rDepth)+1

root = Node(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

inorder(root)

print("\n")

minValue(root)

print("\n")

print(maxDepth(root))

print("\n")

print(search(root, 80))

print("\n")

printLevelOrder(root)

print("\n")

printGivenLevel(root,3)

print("\n")
root = delete(root, 70)

inorder(root)
