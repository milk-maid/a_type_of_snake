weight = input("Enter your weight in kg\n")
height = input("Enter your height in m\n")
h2 = float(height) * float(height)
bmi = int(weight) / h2  # use "//" to print it without the fractional part
# print("If your weight is " + weight + " and your height is " + height + " your BMI is therefore "
# + str(bmi) + "kg/m2")
# aa = str(bmi)
# print(type(aa))
rounded = round(bmi, 2)
# print(type(rounded))
print(f"If your weight is {weight} and your height is {height} your BMI is therefore = {rounded}kg/m2")
if bmi < 16:
    print("You are Severely Underweight")
elif bmi < 17:
    print("You are Moderately Underweight")
elif bmi < 18.5:
    print("You are mildly Underweight")
elif bmi < 25:
    print("You are COOL at the moment (NORMAL)")
elif bmi < 30:
    print("You are OVERWEIGHT(pre-obese)")
elif bmi < 35:
    print("You are OBESE(class I)")
elif bmi < 40:
    print("You are OBESE(class II)")
else:
    print("This is too much OBESITY (class III)")

print("Thanks For Coming Around!!!")