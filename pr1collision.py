class CollisionHandling: 
    def _init_(self): 
        self.linearHash = []  # Hash Table for Linear Probing 
        self.quadraticHash = []  # Hash Table for Quadratic Probing 
        self.linearCount = 0  # No. of comparisons in Linear Probing 
        self.quadraticCount = 0  # No. of comparisons in Quadratic Probing 
        self.bucketSize = 0  # Size of the bucket 
        
    # Function to create Empty Hash Table 
    def create_bucket(self, bsize): 
        self.bucketSize = bsize  
        self.linearHash = [None] * self.bucketSize 
        self.quadraticHash = [None] * self.bucketSize 
        
    # Function to get hash value for the given key 
    def has_key(self, key): 
        return key % self.bucketSize 
        
    ############### Linear Probing ################ 
    def linear_Probing(self, name, phoneNo): 
        pos = self.has_key(phoneNo) 
        index = pos 
        if self.linearHash[pos] is None: 
            self.linearHash[pos] = {name: phoneNo} 
        else:  # Handle collision
            index = (pos + 1) % self.bucketSize 
            while self.linearHash[index] is not None and index != pos: 
                index = (index + 1) % self.bucketSize 
            if self.linearHash[index] is None: 
                self.linearHash[index] = {name: phoneNo} 
            else: 
                return -1  # Table overflow 
        return index 
        
    def search_key_Linear_prob(self, phoneNo): 
        pos = self.has_key(phoneNo) 
        index = pos 
        self.linearCount = 0 
        while self.linearHash[index] is not None: 
            self.linearCount += 1 
            for phone in self.linearHash[index].values(): 
                if phone == phoneNo: 
                    print(f"Phone number found at position {index}") 
                    print(f"Comparisons made: {self.linearCount}")
                    return
            index = (index + 1) % self.bucketSize 
            if index == pos: 
                break 
        print("Phone number not found!") 
        
    def display_Linear_Hash_Table(self): 
        for i in range(self.bucketSize): 
            print(f"{i} -> {self.linearHash[i]}") 

    ############### Quadratic Probing ################ 
    def quadratic_Probing(self, name, phoneNo): 
        pos = self.has_key(phoneNo) 
        i = 0 
        while True:
            index = (pos + i * i) % self.bucketSize
            if self.quadraticHash[index] is None:
                self.quadraticHash[index] = {name: phoneNo}
                return index
            i += 1
            if i == self.bucketSize:  # Full table check
                return -1  
        
    def search_key_quadratic_prob(self, phoneNo): 
        pos = self.has_key(phoneNo)
        i = 0  
        self.quadraticCount = 0  
        
        while True:
            index = (pos + i * i) % self.bucketSize
            if self.quadraticHash[index] is None:
                break
            self.quadraticCount += 1
            for phone in self.quadraticHash[index].values():
                if phone == phoneNo:
                    print(f"Phone number found at position {index}") 
                    print(f"Comparisons made: {self.quadraticCount}")
                    return
            i += 1
            if i == self.bucketSize:  # Prevent infinite loop
                break  
                
        print("Phone number not found!") 
        
    def display_quadratic_Hash_Table(self): 
        for i in range(self.bucketSize): 
            print(f"{i} -> {self.quadraticHash[i]}") 

# Driver Code 
c1 = CollisionHandling()
bsize = int(input("Enter the Size of hash table: "))
c1.create_bucket(bsize) 

while True:
    print("\n** Collision Handling Techniques **") 
    print("1. Linear Probing") 
    print("2. Quadratic Probing") 
    print("3. Exit Application") 
    choice1 = int(input("Enter Your Choice: ")) 

    if choice1 == 1: 
        while True: 
            print("\n** Linear Probing **") 
            print("1. Add Record") 
            print("2. Display Table") 
            print("3. Search Phone Number") 
            print("4. Back to Main") 
            choice2 = int(input("Enter Your Choice: ")) 

            if choice2 == 1:
                name = input("Enter the name: ") 
                phoneNo = int(input("Enter phone number: ")) 
                if c1.linear_Probing(name, phoneNo) == -1:
                    print("\nTable is Full!") 
            elif choice2 == 2: 
                c1.display_Linear_Hash_Table() 
            elif choice2 == 3:
                phoneNo = int(input("Enter the phone number to search: ")) 
                c1.search_key_Linear_prob(phoneNo) 
            elif choice2 == 4:
                break 

    elif choice1 == 2: 
        while True: 
            print("\n** Quadratic Probing **") 
            print("1. Add Record") 
            print("2. Display Table") 
            print("3. Search Phone Number") 
            print("4. Back to Main") 
            choice2 = int(input("Enter Your Choice: ")) 

            if choice2 == 1: 
                name = input("Enter the name: ") 
                phoneNo = int(input("Enter phone number: ")) 
                if c1.quadratic_Probing(name, phoneNo) == -1:
                    print("\nTable is Full!") 
            elif choice2 == 2: 
                c1.display_quadratic_Hash_Table() 
            elif choice2 == 3: 
                phoneNo = int(input("Enter the phone number to search: ")) 
                c1.search_key_quadratic_prob(phoneNo) 
            elif choice2 == 4: 
                break 

    elif choice1 == 3: 
        print("Exiting Application.")
        break

    else:
        print("Invalid Choice! Please enter a valid option.")
