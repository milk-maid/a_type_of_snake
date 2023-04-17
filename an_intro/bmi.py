weight = input("Enter your weight in kg\n")
height = input("Enter your height in m\n")
h2 = float(height) * float(height)
bmi = int(weight) // h2  # to print it without the fractional part
print("If your weight is " + weight + " and your height is " + height + " your BMI is therefore " + str(bmi) + "kg/m2")
