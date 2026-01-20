# WAP to create a new list from existing list which contains cube of each number of list.

li =[20,40,70,10,30,60]

li2 = []
for elem in li:
    li2.append(elem ** 3)

print(li2)