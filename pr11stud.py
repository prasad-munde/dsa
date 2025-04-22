import os

# File to store student data
STUDENT_FILE = "students.txt"

def add_student():
    """Add a new student record"""
    roll_no = input("Enter Roll Number: ")
    
    # Check if student already exists
    if search_student(roll_no, display=False):
        print(f"\nStudent with Roll No {roll_no} already exists!")
        return
    
    # Get student details
    name = input("Enter Name: ")
    division = input("Enter Division: ")
    address = input("Enter Address: ")
    
    # Write to file
    with open(STUDENT_FILE, 'a') as file:
        file.write(f"{roll_no},{name},{division},{address}\n")
    
    print("\nStudent added successfully!")

def search_student(roll_no, display=True):
    """Search for a student by roll number"""
    if not os.path.exists(STUDENT_FILE):
        if display:
            print("\nNo student records exist yet!")
        return False
    
    found = False
    with open(STUDENT_FILE, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[0] == roll_no:
                found = True
                if display:
                    print("\nStudent Found:")
                    print(f"Roll No: {data[0]}")
                    print(f"Name: {data[1]}")
                    print(f"Division: {data[2]}")
                    print(f"Address: {data[3]}")
                break
    
    if not found and display:
        print(f"\nStudent with Roll No {roll_no} not found!")
    
    return found

def delete_student():
    """Delete a student record"""
    roll_no = input("Enter Roll Number to delete: ")
    
    if not os.path.exists(STUDENT_FILE):
        print("\nNo student records exist yet!")
        return
    
    # Create a temporary file
    temp_file = "temp_students.txt"
    found = False
    
    with open(STUDENT_FILE, 'r') as file, open(temp_file, 'w') as temp:
        for line in file:
            data = line.strip().split(',')
            if data[0] != roll_no:
                temp.write(line)
            else:
                found = True
    
    # Replace original file with temp file
    os.replace(temp_file, STUDENT_FILE)
    
    if found:
        print(f"\nStudent with Roll No {roll_no} deleted successfully!")
    else:
        print(f"\nStudent with Roll No {roll_no} not found!")

def display_all_students():
    """Display all student records"""
    if not os.path.exists(STUDENT_FILE):
        print("\nNo student records exist yet!")
        return
    
    print("\n===== All Students =====")
    with open(STUDENT_FILE, 'r') as file:
        records = file.readlines()
        
        if not records:
            print("No student records found!")
            return
            
        for i, line in enumerate(records, 1):
            data = line.strip().split(',')
            print(f"\nStudent {i}:")
            print(f"Roll No: {data[0]}")
            print(f"Name: {data[1]}")
            print(f"Division: {data[2]}")
            print(f"Address: {data[3]}")
            print("-" * 30)

def main_menu():
    """Display the main menu and handle user choices"""
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            roll_no = input("Enter Roll Number to search: ")
            search_student(roll_no)
        elif choice == '3':
            delete_student()
        elif choice == '4':
            display_all_students()
        elif choice == '5':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")

# Create the file if it doesn't exist
if not os.path.exists(STUDENT_FILE):
    open(STUDENT_FILE, 'w').close()

# Start the program
if __name__ == "__main__":
    main_menu()





