print("Welcome To PIZZA HUB!!")

fee = 0
size = input("What size of pizza would you like to have? Small, Medium, or Large-- s/m/l\t")

if size == 's' or size == 'S':
    fee += 100
    print("Small Pizza Costs #100")
elif size == 'm' or size == 'M':
    fee += 200
    print("Medium Pizza Costs #200")
else:
    fee += 300
    print("Large Pizza Costs #300")

pepperoni = input("Would you like to have PEPPERONI added?\t y/n\t")
if pepperoni == 'y' or pepperoni == 'Y':
    if size == 's' or size == 'S':
        fee += 30
        print("Attracts extra charge of #30")
    else:
        fee += 50
        print("Attracts extra charge of #50")
    print("Pepperoni added for you! SWEET!!!")

cheese = input("Would you want extra CHEESE?\t Extra #20\ty/n\t")
if cheese == 'y' or cheese == 'Y':
    fee += 20
    print("Extra Cheese To Your Pizza! AWESOME!!!")

print(f"Your Total Bill is #{fee}")

print("Thanks!!!\tSee you again!!!")
