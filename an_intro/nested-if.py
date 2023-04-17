height = int(input("Enter your height in feet?\n"))

if height >= 6:
    print("You can ride!")
    age = int(input("How old are you?\n"))
    if age <= 18:
        print("Your fee is #25 only")
    else:
        print("You are to pay #45")
else:
    print("We are sorry!!!\nYou can't ride!")
print("Thanks for showing up")
