# Function to construct an Optimal Binary Search Tree (OBST)
def optimal_bst(keys, freq, n):
    # `cost[i][j]` will store the minimum cost of searching for keys[i..j]
    cost = [[0 for _ in range(n)] for _ in range(n)]

    # `root[i][j]` will store the index of the root of the optimal tree
    root = [[0 for _ in range(n)] for _ in range(n)]

    # Single key trees have cost equal to the frequency of that key
    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    # Now we compute the cost for all subtrees of size 2 to n
    for length in range(2, n + 1):  # length is the size of the subproblem
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')  # Initialize to a large value

            # Try making each key in keys[i..j] the root of the tree
            for r in range(i, j + 1):
                # Cost when root is keys[r]
                c = ((cost[i][r - 1] if r > i else 0) +
                     (cost[r + 1][j] if r < j else 0) +
                     sum(freq[i:j + 1]))  # Sum of frequencies from keys[i] to keys[j]

                # Update the minimum cost and root
                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root


# Function to print the structure of the optimal binary search tree
def print_optimal_bst(root, i, j, keys):
    if i > j:
        return

    # Get the root of the optimal BST for keys[i..j]
    r = root[i][j]
    print(f"Root: {keys[r]}")

    # Recursively print the left and right subtrees
    print(f"Left subtree of {keys[r]}:")
    print_optimal_bst(root, i, r - 1, keys)

    print(f"Right subtree of {keys[r]}:")
    print_optimal_bst(root, r + 1, j, keys)


# Function to input keys and their frequencies from the user
def get_user_input():
    # Ask the user for the number of keys
    n = int(input("Enter the number of keys: "))

    # Get the keys and their frequencies
    keys = []
    freq = []

    print("Enter the keys in increasing order:")
    for i in range(n):
        key = int(input(f"Key {i + 1}: "))
        keys.append(key)

    print("Enter the corresponding frequencies for each key:")
    for i in range(n):
        f = int(input(f"Frequency of key {keys[i]}: "))
        freq.append(f)

    return keys, freq, n


# Main function
if __name__ == "__main__":
    # Get the keys and frequencies from the user
    keys, freq, n = get_user_input()

    # Get the cost and root tables for the optimal BST
    cost, root = optimal_bst(keys, freq, n)

    # Print the optimal BST structure
    print("\nOptimal Binary Search Tree:")
    print_optimal_bst(root, 0, n - 1, keys)

    # Print the minimum search cost
    print(f"\nMinimum search cost of the optimal BST: {cost[0][n - 1]}")
