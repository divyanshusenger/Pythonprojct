""" for i in range(1,6):
    for j in range(1,6):
        if(j<=6-i):
            print(6-j, end=" ")
        else:
            print(" ", end = " ")
    print()

5 4 3 2 1 
5 4 3 2
5 4 3
5 4
5 """

""" for i in range(1,6):
    for j in range(1,6):
        if(j<=6-i):
            print(j, end=" ")
        else:
            print(" ", end = " ")
    print()

1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1 """

for i in range(1,6):
    k=i
    for j in range(1,6):
        if(j>=6-i):
            print(k, end=" ")
            k = k+1
        else:
            print(" ", end = " ")
    print()

""" 
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5 """