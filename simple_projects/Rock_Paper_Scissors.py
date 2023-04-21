import random

print("Welcome & Let's Play THe GAME!!!\n")

print("ROCK! PAPER!! SCISSORS!!! Shoot\nEnter Your Choice!")
user = int(input("0 - ROCK\t1- PAPER\t2 - SCISSORS\n"))
comp = random.randint(0, 2)


if user > 2 or user < 0:  # user > 2 and user < 0 >>>> # 2 < user < 0
    print("Invalid Input! 'YOU LOSE'")
else:
    choices = ["ROCK", "PAPER", "SCISSORS"]
    print(f"You Choose is {user} == {choices[user]}!!!")
    print(f"Computer Choice is {comp} == {choices[comp]}!!!")
    if comp == 0 and user == 2:
        print(f"COMPUTER WINS")
    elif comp == 2 and user == 0:
        print(f"YOU WIN")
    elif comp == user:
        print(f"A DRAW THERE")
    elif comp > user:
        print(f"COMPUTER WINS")
    elif comp < user:
        print(f"YOU WIN")

print("Thanks! Always Play Again!")
