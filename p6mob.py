friends = []  # Global list to store (name, mobile) tuples

def insert_friend(name, mobile):
    """Insert friend into the phonebook in sorted order based on name."""
    friend = (name, mobile)
    if friend in friends:
        print(f"{name} is already in the phonebook.")
        return

    # Find the position to insert to keep the list sorted
    position = find_insert_position(name)
    friends.insert(position, friend)
    print(f"{name} has been added to the phonebook.")

def find_insert_position(name):
    """Find the appropriate position to insert the new friend."""
    low, high = 0, len(friends)
    while low < high:
        mid = (low + high) // 2
        if friends[mid][0] < name:
            low = mid + 1
        else:
            high = mid
    return low

def binary_search(name):
    """Perform non-recursive binary search to find a friend's mobile number."""
    low, high = 0, len(friends) - 1
    while low <= high:
        mid = (low + high) // 2
        if friends[mid][0] == name:
            return friends[mid][1]
        elif friends[mid][0] < name:
            low = mid + 1
        else:
            high = mid - 1
    return None

def recursive_binary_search(name, low, high):
    """Perform recursive binary search to find a friend's mobile number."""
    if low > high:
        return None

    mid = (low + high) // 2
    if friends[mid][0] == name:
        return friends[mid][1]
    elif friends[mid][0] < name:
        return recursive_binary_search(name, mid + 1, high)
    else:
        return recursive_binary_search(name, low, mid - 1)

def display_friends():
    """Display the list of friends in the phonebook."""
    if not friends:
        print("The phonebook is empty.")
        return
    print("Phonebook:")
    for name, mobile in friends:
        print(f"{name}: {mobile}")

# Main menu logic
def main():
    while True:
        print("\nMenu:")
        print("1. Insert Friend")
        print("2. Search Friend (Non-Recursive)")
        print("3. Search Friend (Recursive)")
        print("4. Display Friends")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter friend's name: ")
            mobile = input("Enter friend's mobile number: ")
            insert_friend(name, mobile)
        elif choice == '2':
            name = input("Enter friend's name to search: ")
            mobile = binary_search(name)
            if mobile:
                print(f"{name}'s mobile number is: {mobile}")
            else:
                print(f"{name} not found in the phonebook.")
        elif choice == '3':
            name = input("Enter friend's name to search: ")
            mobile = recursive_binary_search(name, 0, len(friends) - 1)
            if mobile:
                print(f"{name}'s mobile number is: {mobile}")
            else:
                print(f"{name} not found in the phonebook.")
        elif choice == '4':
            display_friends()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
