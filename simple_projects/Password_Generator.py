import random

print("Welcome to Your Ultimate Password Generator Platform")

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters.extend(lowercase_letters)
symbols = ['@', '#', '$', '%', '&', '*', '+', '-', '/', '=', '?', '^', '_', '~']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_letters = int(input("How many LETTERS do you want in your password?\n"))
num_numbers = int(input("How many NUMBERS do you want in your password?\n"))
num_symbols = int(input("How many SYMBOL do you want in your password?\n"))
rand = []
# passwd = ""
# password = []
for i in range(num_letters):
    rand.append(random.choice(letters))
    # passwd += random.choice(letters)

for i in range(num_numbers):
    rand.append(random.choice(numbers))

for i in range(num_symbols):
    rand.append(random.choice(symbols))

# for i in range(len(rand)):
#     password.append(random.choice(rand))
# print(password)
# print(''.join(str(x) for x in password))

print(rand)
random.shuffle(rand)

print(rand)
password = ''.join(str(x) for x in rand)
print(f"Your PASSWORD is {password}\nSee You Again!!!")