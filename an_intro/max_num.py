print("WELCOME\nLet's calculate the MAXIMUM NUMBER from a set")

numbers = input("Pass in the numbers separated by space\n")
num_list = numbers.split(" ")
count = 0
for num in num_list:
    count += 1
print("The length of the list is ", count)

for i in range(count):
    num_list[i] = int(num_list[i])

max_num = num_list[0]

for num in num_list:
    if num > max_num:
        max_num = num

print(f"The Maximum number is {max_num}")
