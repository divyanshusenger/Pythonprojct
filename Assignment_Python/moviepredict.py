

""" 
print("1,add")
print("2.mul")
print("3.sub")
print("4.div")

x = int(input("Enter the choice: "))
if (x==1):
    a = int(input("Enter the First value: "))
    b = int(input("Enter the second value: "))
    c = a+b
    print(c)
elif(x==2):
    a = int(input("Enter the First value: "))
    b = int(input("Enter the second value: "))
    c = a*b
    print(c)
elif(x==3):
    a = int(input("Enter the First value: "))
    b = int(input("Enter the second value: "))
    c = a-b
    print(c)
elif(x==4):
    a = int(input("Enter the First value: "))
    b = int(input("Enter the second value: "))
    c = a/b
    print(c)
else:
    print("No Choice")
 """
""" while True:
    print("1.add")
    print("2.mul")
    print("3.sub")
    print("4.div")
    print("5.exit")
    x = int(input("Enter the choice: "))
    if (x==1):
        a = int(input("Enter the First value: "))
        b = int(input("Enter the second value: "))
        c = a+b
        print(c)
    elif(x==2): 
        a = int(input("Enter the First value: "))
        b = int(input("Enter the second value: "))
        c = a*b
        print(c)
    elif(x==3):
        a = int(input("Enter the First value: "))
        b = int(input("Enter the second value: "))
        c = a-b
        print(c)
    elif(x==4):
        a = int(input("Enter the First value: "))
        b = int(input("Enter the second value: "))
        c = a//b
        print(c)
    elif(x==5):
        break
  """
""" # Movie predictor assingnment.
while True:
    print("1.Singham: 300")
    print("2.RRR: 400")
    print("3.Jawan: 500")
    print("4.Kriss: 550")
    print("5.Tigar Zinda hai: 600")
    print("6.exit")
    x= int(input("Enter the choice: "))
    if (x==1):
        a = 300
        b = int(input("Enter the number of people: "))
        c = a*b
        print(c)
    elif(x==2):
        a = 400
        b = int(input("Enter the number of people: "))
        c = a*b
        print(c)
    elif(x==3):
        a = 500
        b = int(input("Enter the number of people: "))
        c = a*b
        print(c)
    elif(x==4):
        a = 550
        b = int(input("Enter the number of people: "))
        c = a*b
        print(c)
    elif(x==5):
        a = 600
        b = int(input("Enter the number of people: "))
        c = a*b
        print(c)
    elif(x==6):
        break  """

while True:
    print("1.Singham: 300")
    print("2.RRR: 400")
    print("3.exist")
    x= int(input("Enter the choice: "))
if(x==1):
    while True:
        print("1. First class - 500")
        print("2. Second class - 300")
        print("3. Third class - 100")
        print("4.exit")
        n = int(input("Enter the choice"))
        if(n==1):
            s = int(input("enter the no of ticket"))
            total = total+s*500
        elif(n==2):
            s = int(input("enter the no of ticket"))
            total = total+s*300
        elif(n==3):
            s = int(input("enter the no of ticket"))
            total = total+s*100
        elif(n==4):
            break
elif(x==2):
    while True:
        print("1. First class - 500")
        print("2. Second class - 300")
        print("3. Third class - 100")
        print("4.exit")
        n = int(input("Enter the choice"))
        if(n==1):
            s = int(input("enter the no of ticket"))
            total = total+s*500
        elif(n==2):
            s = int(input("enter the no of ticket"))
            total = total+s*300
        elif(n==3):
            s = int(input
            ("enter the no of ticket"))
            total = total+s*100
        elif(n==4):
            break
elif(x==3):
    break
print(total)


