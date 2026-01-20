# WAP to print list after removing even numbers.

li = [1,2,3,4,5,6,7,8,9,10]

li2 = []
for elem in li:
    if(elem % 2 != 0):
        li2.append(elem)

li = li2
print(li)