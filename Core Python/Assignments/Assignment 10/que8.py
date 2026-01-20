# WAP to create a duplicate from existing list , it should not point to same list.


li = [10,20,30,40,50]

li2 =[]
for elem in li:
    if elem in li:
        li2.append(elem)

print(li2)
print(id(li))
print(id(li2))
