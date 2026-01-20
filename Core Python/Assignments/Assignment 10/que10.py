# WAP Tto remove all occurances of a given element in the list.


li = [10,20,30,40,20,50]

n = int(input('Enter number'))
li2 = []
for elem in li:
    if n != elem :
        li2.append(elem)
li = li2
print(li)

