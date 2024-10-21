# #  Write a Python program that accepts a word from the user and reverse it. 
# x = str(input("Enter the value: "))
# y = x[::-1]
# print(f"The value of word reverse: {y}")

# 17. Write a Python program to count the number of even and odd numbers from a series of numbers. 
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4


""" numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
even_count = 0
odd_count = 0
for number in numbers:
    if number % 2== 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Number of even numbers: {even_count}")
print(f"Number of ODD numbers: {odd_count}") """


a = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
even = 0
Odd = 0

for i in a:
    if i % 2 == 0:
        even += 1
    else:
        Odd += 1
print(f"Number of even: {even}")
print(f"Number of odds: {Odd}")


