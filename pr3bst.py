class Node:
    def __init__(self, data):  # Fixed __init__ method
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):  # Fixed __init__ method
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def height(self, node):
        if node is None:
            return -1  # Fix: Height of an empty tree is -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    def min_value(self):
        if self.root is None:  # Fix: Check if the tree is empty
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def mirror(self, node):
        if node:
            node.left, node.right = node.right, node.left  # Swap children
            self.mirror(node.left)
            self.mirror(node.right)

    def search(self, node, value):
        if node is None or node.data == value:
            return node
        if value < node.data:
            return self.search(node.left, value)
        return self.search(node.right, value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

# Usage of the BST
bst = BinarySearchTree()

# User input for the BST
print("Enter values to insert into the Binary Search Tree. Enter 'done' when you are finished.")
while True:
    user_input = input("Enter a value: ")
    if user_input.lower() == 'done':
        break
    try:
        value = int(user_input)
        bst.insert(value)
    except ValueError:
        print("Please enter a valid integer.")

# i. Insert new node
new_value = int(input("Enter a new value to insert: "))
bst.insert(new_value)

# ii. Find number of nodes in the longest path from root (height of tree)
print(f"Height (longest path) from root: {bst.height(bst.root)}")

# iii. Find minimum data value
min_val = bst.min_value()
if min_val is not None:
    print(f"Minimum value in the tree: {min_val}")
else:
    print("Tree is empty.")

# iv. Inorder traversal of the original tree
print("Inorder traversal of original tree: ", end="")
bst.inorder(bst.root)
print()

# v. Mirror the tree (swap left and right children)
bst.mirror(bst.root)

# vi. Inorder traversal of the mirrored tree
print("Inorder traversal of mirrored tree: ", end="")
bst.inorder(bst.root)
print()

# vii. Search for a value
value_to_search = int(input("Enter a value to search for: "))
found_node = bst.search(bst.root, value_to_search)
if found_node:
    print(f"Value {value_to_search} found in the tree.")
else:
    print(f"Value {value_to_search} not found in the tree.")
