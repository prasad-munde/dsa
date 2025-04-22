class TreeNode:
    def __init__(self, keyword, meaning):
        self.keyword = keyword
        self.meaning = meaning
        self.left = None
        self.right = None
        self.height = 1  # Height of node in tree

class Dictionary:
    def __init__(self):
        self.root = None
        self.comparisons = 0
    
    # Get height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    # Get balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    # Right rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        
        return x
    
    # Left rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        
        return y
    
    # Add a new keyword and its meaning
    def add(self, keyword, meaning):
        self.comparisons = 0
        self.root = self._add_node(self.root, keyword, meaning)
        return self.comparisons
    
    def _add_node(self, node, keyword, meaning):
        # Normal BST insertion
        if not node:
            return TreeNode(keyword, meaning)
        
        self.comparisons += 1
        if keyword < node.keyword:
            node.left = self._add_node(node.left, keyword, meaning)
        elif keyword > node.keyword:
            node.right = self._add_node(node.right, keyword, meaning)
        else:
            # Update meaning if keyword already exists
            node.meaning = meaning
            return node
        
        # Update height of current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        # Get balance factor to check if node became unbalanced
        balance = self.get_balance(node)
        
        # Left Left Case
        if balance > 1 and keyword < node.left.keyword:
            return self.right_rotate(node)
        
        # Right Right Case
        if balance < -1 and keyword > node.right.keyword:
            return self.left_rotate(node)
        
        # Left Right Case
        if balance > 1 and keyword > node.left.keyword:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # Right Left Case
        if balance < -1 and keyword < node.right.keyword:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    # Find the node with minimum value in a subtree
    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    # Delete a keyword
    def delete(self, keyword):
        self.comparisons = 0
        self.root = self._delete_node(self.root, keyword)
        return self.comparisons
    
    def _delete_node(self, node, keyword):
        if not node:
            return None
        
        self.comparisons += 1
        if keyword < node.keyword:
            node.left = self._delete_node(node.left, keyword)
        elif keyword > node.keyword:
            node.right = self._delete_node(node.right, keyword)
        else:
            # Node to be deleted found
            
            # Node with one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children
            temp = self.get_min_value_node(node.right)
            node.keyword = temp.keyword
            node.meaning = temp.meaning
            node.right = self._delete_node(node.right, temp.keyword)
        
        if not node:
            return None
        
        # Update height
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        
        # Check balance
        balance = self.get_balance(node)
        
        # Left Left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        
        # Left Right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # Right Right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        
        # Right Left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    # Update the meaning of a keyword
    def update(self, keyword, new_meaning):
        return self.add(keyword, new_meaning)  # add will update if keyword exists
    
    # Search for a keyword
    def search(self, keyword):
        self.comparisons = 0
        result = self._search_node(self.root, keyword)
        return result, self.comparisons
    
    def _search_node(self, node, keyword):
        if not node:
            return None
        
        self.comparisons += 1
        if keyword == node.keyword:
            return node.meaning
        elif keyword < node.keyword:
            return self._search_node(node.left, keyword)
        else:
            return self._search_node(node.right, keyword)
    
    # Display all entries in ascending order
    def display_ascending(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.keyword, node.meaning))
            self._inorder(node.right, result)
    
    # Display all entries in descending order
    def display_descending(self):
        result = []
        self._reverse_inorder(self.root, result)
        return result
    
    def _reverse_inorder(self, node, result):
        if node:
            self._reverse_inorder(node.right, result)
            result.append((node.keyword, node.meaning))
            self._reverse_inorder(node.left, result)
    
    # Get maximum possible comparisons (tree height)
    def max_comparisons(self):
        return self.get_height(self.root)
    
    # Count total entries
    def count_entries(self):
        count = [0]
        self._count_nodes(self.root, count)
        return count[0]
    
    def _count_nodes(self, node, count):
        if node:
            count[0] += 1
            self._count_nodes(node.left, count)
            self._count_nodes(node.right, count)


def display_menu():
    print("\n===== DICTIONARY MENU =====")
    print("1. Add a new keyword")
    print("2. Delete a keyword")
    print("3. Update a keyword meaning")
    print("4. Search for a keyword")
    print("5. Display dictionary (Ascending)")
    print("6. Display dictionary (Descending)")
    print("7. Dictionary statistics")
    print("8. Exit")
    print("==========================")
    return input("Enter your choice (1-8): ")


def main():
    dictionary = Dictionary()
    
    # Add some initial sample entries
    sample_data = [
        ("algorithm", "A step-by-step procedure for solving a problem"),
        ("computer", "An electronic device for processing data"),
        ("python", "A high-level programming language"),
        ("dictionary", "A collection of words and their meanings"),
        ("tree", "A data structure with nodes connected by edges")
    ]
    
    print("Initializing dictionary with sample entries...")
    for keyword, meaning in sample_data:
        dictionary.add(keyword, meaning)
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            keyword = input("Enter keyword: ")
            meaning = input("Enter meaning: ")
            comparisons = dictionary.add(keyword, meaning)
            print(f"\nKeyword '{keyword}' added successfully!")
            print(f"Comparisons made: {comparisons}")
        
        elif choice == '2':
            keyword = input("Enter keyword to delete: ")
            comparisons = dictionary.delete(keyword)
            if comparisons > 0:
                print(f"\nKeyword '{keyword}' deleted successfully!")
                print(f"Comparisons made: {comparisons}")
            else:
                print(f"\nKeyword '{keyword}' not found in the dictionary.")
        
        elif choice == '3':
            keyword = input("Enter keyword to update: ")
            new_meaning = input("Enter new meaning: ")
            comparisons = dictionary.update(keyword, new_meaning)
            print(f"\nKeyword '{keyword}' updated successfully!")
            print(f"Comparisons made: {comparisons}")
        
        elif choice == '4':
            keyword = input("Enter keyword to search: ")
            meaning, comparisons = dictionary.search(keyword)
            if meaning:
                print(f"\nKeyword: {keyword}")
                print(f"Meaning: {meaning}")
                print(f"Comparisons made: {comparisons}")
            else:
                print(f"\nKeyword '{keyword}' not found in the dictionary.")
        
        elif choice == '5':
            entries = dictionary.display_ascending()
            if entries:
                print("\n=== Dictionary (Ascending Order) ===")
                for i, (keyword, meaning) in enumerate(entries, 1):
                    print(f"{i}. {keyword}: {meaning}")
            else:
                print("\nDictionary is empty.")
        
        elif choice == '6':
            entries = dictionary.display_descending()
            if entries:
                print("\n=== Dictionary (Descending Order) ===")
                for i, (keyword, meaning) in enumerate(entries, 1):
                    print(f"{i}. {keyword}: {meaning}")
            else:
                print("\nDictionary is empty.")
        
        elif choice == '7':
            print("\n=== Dictionary Statistics ===")
            print(f"Total entries: {dictionary.count_entries()}")
            print(f"Tree height: {dictionary.max_comparisons()}")
            print(f"Maximum comparisons required for lookup: {dictionary.max_comparisons()}")
            print(f"Time complexity: O(log n) where n is the number of entries")
        
        elif choice == '8':
            print("\nThank you for using the Dictionary program. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
