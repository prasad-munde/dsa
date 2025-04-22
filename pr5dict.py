class Node:
    def __init__(self, keyword, meaning):
        self.keyword = keyword
        self.meaning = meaning
        self.left = None
        self.right = None

class DictionaryBST:
    def __init__(self):
        self.root = None

    def insert(self, keyword, meaning):
        self.root = self._insert(self.root, keyword, meaning)
    
    def _insert(self, node, keyword, meaning):
        if node is None:
            return Node(keyword, meaning)
        if keyword < node.keyword:
            node.left = self._insert(node.left, keyword, meaning)
        elif keyword > node.keyword:
            node.right = self._insert(node.right, keyword, meaning)
        else:
            node.meaning = meaning  # Update meaning if keyword exists
        return node
    
    def search(self, keyword):
        return self._search(self.root, keyword, 0)
    
    def _search(self, node, keyword, comparisons):
        if node is None:
            return None, comparisons
        if keyword == node.keyword:
            return node.meaning, comparisons + 1
        elif keyword < node.keyword:
            return self._search(node.left, keyword, comparisons + 1)
        else:
            return self._search(node.right, keyword, comparisons + 1)
    
    def delete(self, keyword):
        self.root = self._delete(self.root, keyword)
    
    def _delete(self, node, keyword):
        if node is None:
            return node
        if keyword < node.keyword:
            node.left = self._delete(node.left, keyword)
        elif keyword > node.keyword:
            node.right = self._delete(node.right, keyword)
        else:
            # Node with the keyword found, now delete
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children, get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(node.right)
            node.keyword, node.meaning = temp.keyword, temp.meaning  # Copy inorder successor's content to this node
            node.right = self._delete(node.right, temp.keyword)  # Delete inorder successor
        return node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append((node.keyword, node.meaning))
            self._inorder(node.right, result)
    
    def reverse_inorder(self):
        result = []
        self._reverse_inorder(self.root, result)
        return result
    
    def _reverse_inorder(self, node, result):
        if node is not None:
            self._reverse_inorder(node.right, result)
            result.append((node.keyword, node.meaning))
            self._reverse_inorder(node.left, result)
    
    def max_comparisons(self):
        return self._max_depth(self.root)
    
    def _max_depth(self, node):
        if node is None:
            return 0
        left_depth = self._max_depth(node.left)
        right_depth = self._max_depth(node.right)
        return max(left_depth, right_depth) + 1

# Example Usage
dictionary = DictionaryBST()

# Adding entries to the dictionary
dictionary.insert("apple", "A fruit")
dictionary.insert("banana", "A yellow fruit")
dictionary.insert("cat", "A small domesticated carnivorous mammal")
dictionary.insert("dog", "A domesticated carnivorous mammal")
dictionary.insert("elephant", "A large herbivorous mammal")

# Display dictionary in ascending order (alphabetically)
print("Ascending Order (Sorted by keyword):", dictionary.inorder())

# Display dictionary in descending order (reverse alphabetical)
print("Descending Order:", dictionary.reverse_inorder())

# Searching for a keyword
keyword = input("Enter keyword to search: ")
meaning, comparisons = dictionary.search(keyword)
if meaning:
    print(f"Meaning of {keyword}: {meaning} (Found in {comparisons} comparisons)")
else:
    print(f"Keyword {keyword} not found")

# Deleting a keyword from the dictionary
keyword_to_delete = input("Enter keyword to delete: ")
dictionary.delete(keyword_to_delete)
print(f"After deleting keyword '{keyword_to_delete}':")

# Display dictionary after deletion
print("Ascending Order (After Deletion):", dictionary.inorder())

# Maximum comparisons required for search
print("Maximum Comparisons Required:", dictionary.max_comparisons())
