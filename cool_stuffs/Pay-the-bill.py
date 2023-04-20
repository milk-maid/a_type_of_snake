import random
print("Let's help you select who pays the bill at RANDOM")

name = input("Enter everybody's name separated by comma?\n")
names = name.split(",")

head_count = len(names)
rand = random.randrange(0, head_count)
chosen = names[rand]
print(f"The names are:\n{names}\n")
print(f"The Chosen One for the payment is at index number {rand} in person of::: {chosen}. HURRAY!!!")
print("Thank You And GOD Bless You All!!!")
