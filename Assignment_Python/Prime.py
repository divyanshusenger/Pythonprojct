'''Given no is a prime no or not.
x = int(input("Enter the value"))
if x==1:
    print("It is not a prime no:")
if x>=1:
    for i in range(2, x):
        if x%i==0:
            print("Not the prime number")
            break
        else:
            print("It is a prime number")'''

''''3. Display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

for i in range(5, 151):
    if i>150:
        break
    if i%5==0:
        print(i)'''

'''import keyword
print(keyword.kwlist)'''

''' Given a number count the total number of digits in a number.'''
""" numbers = [1,4,5,6,5,4,3,8,2,1]
count = 0
for i in numbers:
    if i>2:
        count += 1
    print("there are {count} of numbers is greater than 2") """

""" Implement a system where the user can select multiple items from a menu, input the quantity, and get the total bill.
Add an option to exit or continue shopping. """

""" while True:
    print("1. Air Conditioner: 45098" )
    print("2. Water cooler: 12432")
    print("3. Freez: 15678")
    print("4. Lapotop: 45000")
    print("5. Exit")
    x = int(input("Enter the Choices: "))
    if(x==1):
        a= 45098
        b= int(input("Enter the number of itoms: "))
        c =a*b
        print(c)
    elif(x==2):
        a= 12432
        b= int(input("Enter the number of itoms: "))
        c =a*b
        print(c)
    elif(x==3):
        a= 15678
        b= int(input("Enter the number of itoms: "))
        c =a*b
        print(c)
    elif(x==4):
        a= 45000
        b= int(input("Enter the number of itoms: "))
        c =a*b
        print(c)
    elif(x==5):
        break """

balance = 1000
while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print(f"Your balance is: ${balance}")
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"New balance: ${balance}")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"New balance: ${balance}")
    elif choice == 4:
        break
    else:
        print("Invalid choice, try again.")

    
    







