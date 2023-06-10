print("Lets Check For Primality!!!")

num = int(input("Enter the number you want to check it's primality\n"))
yes = True

if num < 2:
    print(f"{num} is a  Prime number")
for i in range(2, num//2 + 1):

    if num % i == 0:
        print("divisible by ", i)
        yes = False
        break

if yes:
    print(f"{num} is Prime number")
else:
    print(f"{num} is NOT Prime number")

