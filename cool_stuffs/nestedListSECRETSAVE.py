print("Welcome!!!")

nestedlist = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]
# nestedlist[2][1] = "X"
# nestedlist[0][0] = "X"
# print(f"{nestedlist[0]}\n{nestedlist[1]}\n{nestedlist[2]}")
position = input("Enter a two digit position you'll like to save your treasure SECRETLY btw 0-2\t")

row = int(position[0])
col = int(position[1])
nestedlist[row][col] = "X"
print(f"{nestedlist[0]}\n{nestedlist[1]}\n{nestedlist[2]}")
print("Thanks For Coming!!!")
