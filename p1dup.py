def duplibooks(books):
    unqbook =[]
    for book in books:
        if book not in unqbook:
            unqbook.append(book)
    return unqbook

def ascend(books):
    sortbook = books[:]
    for i in range(len(sortbook)):
        for j in range(i+1,len(sortbook)):
            if sortbook[i][2]>sortbook[j][2]:
             sortbook[i],sortbook[j]=sortbook[j],sortbook[i]
    return sortbook

def count(books):
    count = 0
    for book in books:
     if book[2]>500:
        count+=1
    return count

def less(books):
    copy=[]
    for book in books:
      if book[2]<500:
        copy.append(book)

    return copy



N = int(input("enter number of books"))

lib =[]

for i in range(N):
    name = input("enter the name")
    author = input("enter the author")
    cost = int(input("enter the cost"))
    lib.append((name,author,cost))


dup=duplibooks(lib)

sort = ascend(lib)

more = count(lib)

cheap = less(lib)

print("unqie book")
for book in dup:
    print(book)

print("ascending order")
for book in sort:
   print(book)

print("cost more than 500",more)

print("less than 500")
for book in cheap:
   print(book)
