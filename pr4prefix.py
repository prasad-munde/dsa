class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class ExpressionTree:
    def _init_(self):
        self.root = None

    def construct_from_prefix(self, prefix):
        stack = []
        # Reverse the prefix expression to process from left to right
        for char in reversed(prefix):
            if char.isalnum():  # If operand (a-z or 0-9)
                node = Node(char)
                stack.append(node)
            else:  # If operator
                node = Node(char)
                # Pop two elements from the stack for the operands
                node.left = stack.pop()
                node.right = stack.pop()
                stack.append(node)
        self.root = stack.pop()

    def post_order_traversal_non_recursive(self):
        if not self.root:
            return []

        # Two stacks approach
        result = []
        stack = []
        last_visited_node = None
        current_node = self.root

        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                peek_node = stack[-1]
                # If the right child is None or already visited, visit the node
                if peek_node.right and last_visited_node != peek_node.right:
                    current_node = peek_node.right
                else:
                    result.append(peek_node.data)
                    last_visited_node = stack.pop()
                    current_node = None
        return result

    def delete_tree(self):
        self.root = None  # Python garbage collection will handle the rest

# Main Execution
expression = "+--a*bc/def"
tree = ExpressionTree()
tree.construct_from_prefix(expression)

# Post-order traversal (non-recursive)
post_order_result = tree.post_order_traversal_non_recursive()
print("Post-order traversal result:", "".join(post_order_result))

# Deleting the tree (will be handled automatically by Python's garbage collection)
tree.delete_tree()
print ("Tree deleted.")
