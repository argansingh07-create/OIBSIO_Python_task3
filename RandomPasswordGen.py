#Making random password genrator program 
#By_Argan Singh

import random
import string

s1=string.digits
s2=string.ascii_letters
s3=string.printable

print("Welcome to Random Password genrator Program !!")

letters=int(input("Enter How many letters  you want in your password : "))
numbers=int(input("Enter How many digits you want in yor password : "))
symbols=int(input("Enter How many symbol you want in your password : "))
password=""


for i in range(1,letters+1):
    char=random.choice(list(s2))
    password=password+char
    
for i in range(1,numbers+1):
    char=random.choice(list(s1))
    password=password+char
    
for i in range(1,symbols+1):
    char=random.choice(list(s3))
    password=password+char
    
print(password)          

print("Thanks for using this Program")
