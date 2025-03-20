class SetOperations: 
    def __init__(self):  # Fixed constructor name
        self.setA = set()  
        self.setB = set()  
        self.setC = set()  

    # Add element to set A
    def add_element_setA(self, element):
        self.setA.add(element)

    # Add element to set B
    def add_element_setB(self, element):
        self.setB.add(element)

    # Remove element from set A
    def remove_element_setA(self, element):
        if element in self.setA:
            self.setA.remove(element)
        else:
            print("Element not found in Set A")

    # Remove element from set B
    def remove_element_setB(self, element):
        if element in self.setB:
            self.setB.remove(element)
        else:
            print("Element not found in Set B")

    # Check if element exists in set A
    def constraints_setA(self, element):
        print(f"{element} {'is' if element in self.setA else 'is not'} found in Set A")

    # Check if element exists in set B
    def constraints_setB(self, element):
        print(f"{element} {'is' if element in self.setB else 'is not'} found in Set B")

    # Get the size of set A
    def size_setA(self):
        return len(self.setA)

    # Get the size of set B
    def size_setB(self):
        return len(self.setB)

    # Display the elements of set A
    def display_setA(self):
        print(f"Set A: {self.setA}")

    # Display the elements of set B
    def display_setB(self):
        print(f"Set B: {self.setB}")

    # Set Intersection (A ∩ B)
    def set_intersection(self):
        self.setC = self.setA & self.setB
        print(f"Intersection of Set A and Set B: {self.setC}")

    # Set Union (A ∪ B)
    def set_union(self):
        self.setC = self.setA | self.setB
        print(f"Union of Set A and Set B: {self.setC}")

    # Set Difference (A - B)
    def set_difference(self):
        self.setC = self.setA - self.setB
        print(f"Difference of Set A and Set B (A - B): {self.setC}")

# Driver Code
if __name__ == "__main__": 
    c1 = SetOperations()
    
    while True:
        print("\n ***SET OPERATIONS***")
        print("1. Add new element in Set A")
        print("2. Add new element in Set B")
        print("3. Remove element from Set A")
        print("4. Remove element from Set B")
        print("5. Check if element is in Set A")
        print("6. Check if element is in Set B")
        print("7. Check the size of Set A")
        print("8. Check the size of Set B")
        print("9. Display Set A")
        print("10. Display Set B")
        print("11. Set Intersection (A ∩ B)")
        print("12. Set Union (A ∪ B)")
        print("13. Set Difference (A - B)")
        print("14. Exit")

        try:
            choice1 = int(input("\nEnter your choice: "))

            if choice1 == 1:
                element = int(input("Enter element to add to Set A: "))
                c1.add_element_setA(element)
            elif choice1 == 2:
                element = int(input("Enter element to add to Set B: "))
                c1.add_element_setB(element)
            elif choice1 == 3:
                element = int(input("Enter element to remove from Set A: "))
                c1.remove_element_setA(element)
            elif choice1 == 4:
                element = int(input("Enter element to remove from Set B: "))
                c1.remove_element_setB(element)
            elif choice1 == 5:
                element = int(input("Enter element to check in Set A: "))
                c1.constraints_setA(element)
            elif choice1 == 6:
                element = int(input("Enter element to check in Set B: "))
                c1.constraints_setB(element)
            elif choice1 == 7:
                print("Size of Set A:", c1.size_setA())
            elif choice1 == 8:
                print("Size of Set B:", c1.size_setB())
            elif choice1 == 9:
                c1.display_setA()
            elif choice1 == 10:
                c1.display_setB()
            elif choice1 == 11:
                c1.set_intersection()
            elif choice1 == 12:
                c1.set_union()
            elif choice1 == 13:
                c1.set_difference()
            elif choice1 == 14:
                print("Exiting Program...")
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
