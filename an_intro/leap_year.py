year = int(input("What year do you want to check???\t"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"...This year: {year} is a LEAP YEAR")
        else:
            print(f"...This year: {year} is a definitely NOT LEAP YEAR")
    else:
        print(f"..This year: {year} is a LEAP YEAR")
else:
    print(f".This year: {year} is a definitely NOT LEAP YEAR")

print("Thanks for using our app?!!!")

