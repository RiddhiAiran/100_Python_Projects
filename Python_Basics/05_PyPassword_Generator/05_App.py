import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_']

print("Welcome to the PyPassword Generator!")

n_letters = int(input("How many letters would you like in your password?\n"))
n_numbers = int(input("How many numbers would you like?\n"))
n_symbols = int(input("How many symbols would you like?\n"))

password_list = []

for char in range(0,n_letters):
    password_list.append(random.choice(letters))

for num in range(0,n_numbers):
    password_list.append(random.choice(numbers))

for sym in range(0,n_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += char
print(f"Your Password is : {password}")