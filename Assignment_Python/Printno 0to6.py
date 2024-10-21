""" 18. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5 """

for i in range(6):
    if i == 3 or i==6:
        continue
    print(i, end= " ") 

# Question 3: Write a Python program that prints all the numbers from 1 to 20 except for those that are multiples of 5.
""" 
for i in range(1,20):
    if i%5== 0:
        continue
    print(i, end= " ")
 """




# while(True):
#         i = int(input("Enter the value: "))
#         if(i>100):
#               print("Congratulation your Number is greater than Zero")
#               breakh
#         else:
#                print("TRy again") """
        