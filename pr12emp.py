import os
import json

class EmployeeManagementSystem:
    def __init__(self, data_file='employees.dat', index_file='index.dat'):
        self.data_file = data_file
        self.index_file = index_file
        self.index = {}
        
        # Load existing index if available
        if os.path.exists(self.index_file):
            with open(self.index_file, 'r') as f:
                self.index = json.load(f)
    
    def save_index(self):
        with open(self.index_file, 'w') as f:
            json.dump(self.index, f)
    
    def add_employee(self, emp_id, name, designation, salary):
        # Check if employee already exists
        if str(emp_id) in self.index:
            print(f"Employee with ID {emp_id} already exists.")
            return False
        
        # Create employee record
        employee = {
            'emp_id': emp_id,
            'name': name,
            'designation': designation,
            'salary': salary
        }
        
        # Append to data file and update index
        with open(self.data_file, 'a') as f:
            position = f.tell()
            f.write(json.dumps(employee) + '\n')
        
        self.index[str(emp_id)] = position
        self.save_index()
        print(f"Employee {name} added successfully.")
        return True
    
    def delete_employee(self, emp_id):
        emp_id = str(emp_id)
        if emp_id not in self.index:
            print(f"Employee with ID {emp_id} does not exist.")
            return False
        
        # Mark as deleted in index (we'll just remove the entry)
        del self.index[emp_id]
        self.save_index()
        
        # Note: In a real system, you might want to mark the record as deleted in the data file
        # or periodically rebuild the file to remove deleted records
        print(f"Employee with ID {emp_id} deleted successfully.")
        return True
    
    def display_employee(self, emp_id):
        emp_id = str(emp_id)
        if emp_id not in self.index:
            print(f"Employee with ID {emp_id} does not exist.")
            return False
        
        position = self.index[emp_id]
        
        with open(self.data_file, 'r') as f:
            f.seek(position)
            line = f.readline()
            try:
                employee = json.loads(line)
                print("\nEmployee Details:")
                print(f"ID: {employee['emp_id']}")
                print(f"Name: {employee['name']}")
                print(f"Designation: {employee['designation']}")
                print(f"Salary: {employee['salary']}")
                return True
            except json.JSONDecodeError:
                print("Error reading employee data.")
                return False
    
    def display_all_employees(self):
        if not self.index:
            print("No employees in the system.")
            return
        
        print("\nAll Employees:")
        for emp_id, position in self.index.items():
            with open(self.data_file, 'r') as f:
                f.seek(position)
                line = f.readline()
                try:
                    employee = json.loads(line)
                    print(f"ID: {employee['emp_id']}, Name: {employee['name']}, Designation: {employee['designation']}, Salary: {employee['salary']}")
                except json.JSONDecodeError:
                    print(f"Error reading data for employee ID {emp_id}")

def main():
    ems = EmployeeManagementSystem()
    
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Display Employee")
        print("4. Display All Employees")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                emp_id = int(input("Enter Employee ID: "))
                name = input("Enter Name: ")
                designation = input("Enter Designation: ")
                salary = float(input("Enter Salary: "))
                ems.add_employee(emp_id, name, designation, salary)
            except ValueError:
                print("Invalid input. Please enter valid data.")
        
        elif choice == '2':
            try:
                emp_id = int(input("Enter Employee ID to delete: "))
                ems.delete_employee(emp_id)
            except ValueError:
                print("Invalid Employee ID. Please enter a number.")
        
        elif choice == '3':
            try:
                emp_id = int(input("Enter Employee ID to display: "))
                ems.display_employee(emp_id)
            except ValueError:
                print("Invalid Employee ID. Please enter a number.")
        
        elif choice == '4':
            ems.display_all_employees()
        
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

