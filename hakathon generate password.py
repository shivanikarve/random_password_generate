# import string
# import random

# characters = list(string.ascii_letters + string.digits + "!@#$5^&*()")
# def generate_random_password():
#     length = int(input("enter password length : "))
#     random.shuffle(characters)
#     password = []
#     for i in range(length):
#         password.append(random.choice(characters))
#     random.shuffule(password)
#     print("".join(password))
# generate_random_password
    

import string 
import random
print("hello,welcome to password generate")
length=int(input("enter the no"))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation
all=lower+upper+num+symbols
b=list(all)
random.shuffle(b)
tem=random.sample(b,length)
password="".join(tem)
print(password)
