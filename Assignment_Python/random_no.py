""" import random

# Generate a random number between 1 and 9
random_number = random.randint(1, 9)

print("Enter the guess number between 1 to 9")
num = int(input())

if num == random_number:
     print(random_number)
    print("Well guessed")
else:
    while num != random_number:
        print("Your guess is wrong, try again")
        
        # Generate a new random number between 1 and 9
        random_number = random.randint(1, 9)
        print(random_number)
        print("Enter the guess number between 1 to 9")
        num = int(input())
        
        if num == random_number:
            print("Well guessed")
            break
  """

# 14. Write a Python program to guess a number between 1 to 9. 
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.


import random
guess_number = random.randint(1,9)

while True:
    print(guess_number)
    x = int(input("Enter the guess no: "))
    if x == guess_number:
        print("Well guess")
        break
    else:
        print("Wrong guess")