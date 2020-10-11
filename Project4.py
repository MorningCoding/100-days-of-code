#Oct 10, 2020; Password Generator
import string
import random
from random import *

#function that can generate passwords of 10 characters
def password_creator(x):
    #contains a list of letters, punctuation and digits to random select from
    container = list(string.ascii_letters + string.punctuation + string.digits)
    #empty string of new password
    new_password=""
    #set the number of characters you want the password to be
    for i in range(x):
        new_password+=choice(container)
    return (new_password)

#call the function
print(password_creator(10))