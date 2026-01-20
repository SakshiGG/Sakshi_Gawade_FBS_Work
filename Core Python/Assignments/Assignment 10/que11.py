# WAP to print all numbers which are divisible by m and n in the list.

li = [10,29,34,12,34,56,90]

m = int(input('Enter Number:'))
n = int(input('Enter Number:'))

li2 = []
for elem in li:
    if(elem % m==0 and elem % n ==0):
        li2.append(elem)

print(li2)
