"""


name = input("What is your name?\n")
length = len(name)
print(name)
print("Your name has " + str(length) + " characters") #===TYPECASTED AN int TO A str===
print("type of len() is " + str(type(length))) #===using TYPE

"""

# ========= for TYPE CASTING/CONVERSION ===========
"""
int()
float()
str()
"""

#  TASK ==============[ADD TWO NUMBERS]================

first = input("Enter a number: \n")
second = input("Enter another number: \n")

add = int(first) + int(second)
print("The addition of your input " + first  + " + " + second + " is " + str(add))
