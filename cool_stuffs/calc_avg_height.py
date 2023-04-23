print("WELCOME\nLet's calculate AVERAGE")

height = input("Pass in the heights separated by space\n")

split_height = height.split(" ")

# heights = [5.4, 7.9, 6.8, 7, 4]
# print(sum(heights))
addition = 0
count = 0
for height in split_height:
    count += 1

for i in range(count):
    split_height[i] = int(split_height[i])
    # print(split_height)
    addition += split_height[i]
else:
    print(addition)
    print(count)
    print(f"The average of the heights is {addition / count}\nThanks!!!")
