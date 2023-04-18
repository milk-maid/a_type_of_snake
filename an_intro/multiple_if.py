print("Wellcome to the ROLLER-COASTER!!!")

height = int(input("Enter Your Height In Feet?\t"))
fee = 0

if height >= 4:
    age = int(input("What's your age last birthday?\t"))
    if age < 12:
        fee += 150
        print("Ticket Fee is #150")
    elif age <= 18:
        fee += 250
        print("Ticket Fee is #250")
    else:
        fee += 500
        print("Ticket Fee is #500")
    photos = input("Do you want Photos?\t Y/N\t")
    if photos == 'y' or photos == 'Y':
        fee += 50

    print(f"Your Total Bill is #{fee}")
else:
    print("We are Sorry! You are not eligible to ride for now")

print("Thanks for your Interest\nYou're always welcome@@@")