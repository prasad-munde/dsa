# FUNCTION TO DELETE DUPLICATE ENTRIES FROM A LIST 
def delete_duplicate(books): 
    unique_books = [] 
    for book in books: 
        if book not in unique_books: 
            unique_books.append(book) 
    return  unique_books 

# FUNCTION TO SORT BOOKS IN ASCENDING ORDER BAISED ON COST 
def sort_books(books): 
    sorted_books = books [:] #CREATING A COPY OF ORIGINAL LIST 
    for i in range(len(sorted_books)): 
        for j in range (i+1, len(sorted_books)): 
            if sorted_books[i][2]>sorted_books[j][2]: 
                sorted_books[i],sorted_books[j] = sorted_books[j],sorted_books[i] 
    return sorted_books 

# FUNCTION TO COUNT BOOKS WITH COST MORE THAN 500 
def count_expensive(books): 
    count = 0 
    for book in books: 
        if book [2]>500: 
            count += 1 
    return count 

#FUNCTION TO COPY BOOKS WITH COST LESS THAN 500 TO A NEW LIST 
def copy_cheap_books(books): 
    cheap_books = [] 
    for book in books: 
        if book [2] <500: 
            cheap_books.append(book) 
    return cheap_books 

#MAIN FUNCTION 
N = int (input ("Enter the number of books:")) 
library = [] 
for i in range (N): 
    title = input (f"Enter the title of the book {i+1}:") 
    author = input (f"Enter the author of the book {i+1}:") 
    cost = float (input (f"Enter the cost of the book {i+1}:")) 
    library.append((title, author, cost)) 

# DELETING DUPLICATE ENTRIES 
library = delete_duplicate(library) 

# SORTING BOOK COST IN ASCENDING ORDER 
sorted_library = sort_books(library) 

# COUNTING BOOKS WITH COST MORE THAN 500 
expensive_count = count_expensive(sorted_library) 

# COPYING BOOKS WITH COST LESS THAN 500 
cheap_library = copy_cheap_books(sorted_library) 

# DISPLAY RESULT 
print ("\n UNIQUE BOOKS:") 
for book in library: 
    print(book) 
print ("\n BOOKS SORTED BY COST:") 
for book in sorted_library: 
    print(book) 
print ("\n COUNT OF BOOKS WITH COST GREATER THAN 500:", expensive_count) 
print ("\n BOOKS WITH COST LESS THAN 500:") 
for book in cheap_library: 
    print(book) 
