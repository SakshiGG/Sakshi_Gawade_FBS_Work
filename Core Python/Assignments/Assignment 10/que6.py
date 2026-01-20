# WAP to remove duplicates from the list.

li =[20,40,70,20,10,30,60,10]

li2 = []
for elem in li:
    if elem not in li2:
        li2.append(elem)

li = li2
print(li)


