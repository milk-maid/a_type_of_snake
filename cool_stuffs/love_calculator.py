print("Welcome! Let's see if you're in truly in LOVE!!!")

partner1 = input("What's your name?\t")
partner2 = input("What's  your partner's name\t")

name_string = partner1 + partner2

lower_case_name_string = name_string.lower()

t = lower_case_name_string.count('t')
r = lower_case_name_string.count('r')
u = lower_case_name_string.count('u')
e = lower_case_name_string.count('e')

true = t + r + u + e

l = lower_case_name_string.count('l')
o = lower_case_name_string.count('o')
v = lower_case_name_string.count('v')
e = lower_case_name_string.count('e')

love = l + o + v + e

love_rate = int(str(true) + str(love))
if love_rate < 10 or love_rate > 90:
    print(f"Your love score is {love_rate}, so you two go together like coke and bread")
elif 40 <= love_rate <= 50:  # 40 <= love_rate <= 50 ==== love_rate >= 40 and love_rate <= 50
    print(f"Your love score is {love_rate}, so you are alright together!")
else:
    print(f"Your love score is {love_rate}")

print("Thanks For Showing Up!!!")
