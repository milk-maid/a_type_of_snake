print("The sum of een numbers from 0 to and including 100")

a = range(0, 101)
ans = 0
even_list = []
for i in a:
    if i % 2 == 0:
        even_list.append(i)
        ans += i
print(f"The list of the even numbers added is :::\n{even_list}")
print("The answer is ", ans)
