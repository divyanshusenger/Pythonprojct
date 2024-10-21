"""  Write a Python program to get the Fibonacci series between 0 to 50. 
   Note : The Fibonacci Sequence is the series of numbers :
   0, 1, 1, 2, 3, 5, 8, 13, 21, ....
  Every next number is found by adding up the two numbers before it.
  Expected Output : 0 1 1 2 3 5 8 13 21 34 """
""" n= int(input("Enter the value: "))
x=0
y=1
y=1
z=0
while(z<=n):
    print(z, end=" ")
    x=y
    y=z
    z=x+y """

""" #  Find GCD of two Numbers
k=1
for i in range(1,10):
  if i<=5:
    k= i
  else:
    k=10-i
  for j in range(1,6):
    if j<=k:
      print("*", end= " ")
    else:
      print(" ", end=" ")
  print()      """

# k=1
# for i in range(1,10):
#     if i<=5:
#        k=6-i
#     else:
#        k=i-4
#     for j in range(1,6):
#         if j>=k:
#           print("*",end=" ")
#         else:
#            print(" ",end=" ")
#     print()
""" 
for i in range(63, 91):
  print(chr(i),end=" ") """
""" 
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

if num2>num1:
  mn= num1
else:
  mn = num2
for i in range(1, mn+1):
  if num1%i==0 and num2%i==0:
    hcf=i
print(f"Enter the HCF/GCD of these two number {hcf}")  """
""" 
#  Find LCM of two Numbers.
num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))
maxnum = max(num1, num2)
while(True):
  if (maxnum%num1==0 and maxnum%num2==0):
    break
  maxnum = maxnum +1

print(f"The LCM of {num1} and {num2} is {maxnum}" ) """

#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
# result= []
# for num in range(1500, 2701):
#     if (num%7==0 and num%5==0):
#         result.append(num)
# print(result)

#  Write a Python program to guess a number between 1 to 9. 
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random
guess_number = random.randint(1,9)

