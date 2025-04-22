class Patient:
    def __init__(self, name, condition):
        self.name = name
        # Set priority based on condition
        if condition.lower() == "serious":
            self.priority = 1  # Top priority
        elif condition.lower() == "non-serious":
            self.priority = 2  # Medium priority
        else:  # General checkup
            self.priority = 3  # Least priority
        self.condition = condition
    
    def __str__(self):
        return f"{self.name} - {self.condition}"


class HospitalQueue:
    def __init__(self):
        self.queue = []
    
    def add_patient(self, patient):
        """Add a patient to the queue based on priority"""
        # Add patient to queue
        self.queue.append(patient)
        # Sort queue by priority
        self.queue.sort(key=lambda x: x.priority)
    
    def treat_next_patient(self):
        """Remove and return the highest priority patient"""
        if not self.queue:
            return None
        return self.queue.pop(0)
    
    def show_queue(self):
        """Display all patients in the queue"""
        if not self.queue:
            print("\nNo patients in the queue.")
            return
        
        print("\nCurrent Queue (in order of treatment):")
        print("-" * 40)
        for i, patient in enumerate(self.queue, 1):
            priority_text = ""
            if patient.priority == 1:
                priority_text = "Serious (High Priority)"
            elif patient.priority == 2:
                priority_text = "Non-Serious (Medium Priority)"
            else:
                priority_text = "General Checkup (Low Priority)"
            
            print(f"{i}. {patient.name} - {priority_text}")
        print("-" * 40)


# Main program
def main():
    hospital = HospitalQueue()
    
    while True:
        print("\n==== Hospital Priority Queue ====")
        print("1. Add a new patient")
        print("2. Treat next patient")
        print("3. View all patients")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter patient name: ")
            
            print("\nSelect patient condition:")
            print("1. Serious (Top priority)")
            print("2. Non-Serious (Medium priority)")
            print("3. General Checkup (Least priority)")
            
            condition_choice = input("Enter choice (1-3): ")
            
            if condition_choice == '1':
                condition = "Serious"
            elif condition_choice == '2':
                condition = "Non-Serious"
            elif condition_choice == '3':
                condition = "General Checkup"
            else:
                print("Invalid choice! Setting as General Checkup.")
                condition = "General Checkup"
            
            new_patient = Patient(name, condition)
            hospital.add_patient(new_patient)
            print(f"\n{name} added with {condition} condition.")
        
        elif choice == '2':
            patient = hospital.treat_next_patient()
            if patient:
                print(f"\nNow treating: {patient}")
            else:
                print("\nNo patients in the queue.")
        
        elif choice == '3':
            hospital.show_queue()
        
        elif choice == '4':
            print("\nExiting the program. Goodbye!")
            break
        
        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
