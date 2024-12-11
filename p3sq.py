def square(n):
    magicsquare =[[0 for x in range(n)]for y in range(n)]
    i=n/2
    j=n-1

    num =1
    while num<=(n*n):
        if i==-1 and j==n:
            i=0
            j=n-2
        else:
            if j==n:
                j=0
            if i<0:
                i=n-1

        if magicsquare[int(i)][int(j)]:
            i=i+1
            j=j-2
            continue
        else:
            magicsquare[int(i)][int(j)] = num
            num=num+1

        i=i-1
        j=j+1

    print(n)
    print("sum of row", n*(n*n+1)/2)

    for i in range(0,n):
        for j in range(0,n):
            print('%2d ' % (magicsquare[i][j]),end =' ')

            if j== n-1:
                print()


square(3)

