'''Write a Python program to generate a random 
password consisting of lower case and upper case 
characters along with numbers.You can also use 
the random module for shuffling the password 
generated.'''

import random
import string
pass_len = 12
charValues = string.ascii_letters 
password = "".join([random.choice(charValues)

for i in range(pass_len)])
print("Your random password is :", password)