# 19. Write a Python program that accepts a string and calculate the number of digits and letters.

A = input("Enter the string: ")
ct_letter = 0
ct_digit = 0
for i in A:
    if(i>="a" and i<="z" or i>="A" and i<="Z"):
        ct_letter += 1
    if(i >="0" and i<="9"):
        ct_digit +=1
print(f"Enter the ct_letter: {ct_letter}")
print(f"Enter the ct_digit: {ct_digit}")
