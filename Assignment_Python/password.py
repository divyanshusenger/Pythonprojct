""" 20. Write a Python program to check the validity of password input by users. 
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters. """

"""def password_validator(password):
    special_char      = ['@', '#', '$', '%', '&', '%']
    isLengthok        = True if len(password)>=6 and len(password)<20 else False
    isDigit_present   = any(char.isdigit() for char in password)
    isLower_present   = any(char.islower() for char in password) 
    isUpper_present   = any(char.isupper() for char in password)
    isSpecial_present = any(char  in special_char for char in password)
    is_valid = all([isLengthok, isDigit_present, isLower_present, isUpper_present, isSpecial_present])
    if is_valid:
        print("valid password !!, GO Ahead...")
    else:
        print("Wrong password !!, Check the policy of password !!\n")


password_validator("Divya#123") """




""" for i in range(69, 64, -1):
    for j in range(65,70):
        if(j<=i):
            print(chr(j), end=" ")
        else:
            print(" ", end=" ")
    print() """



# print("Divyanshu is the good boy", end=" ")
# print("Anurag is the good boy also")


""" for i in range(1,6):
    for j  in range(1,6):
        if(j>=i):
            print('*', end=" ")
        else:
            print(" ", end=" ")
    print() """

for i in range(0,5):
    for k in range (0,i):
        print(" ", end=" ")
    for j in range(5,i,-1):
        print("*", end=" ")
    print()