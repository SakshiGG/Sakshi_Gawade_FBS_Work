# WAP to find the second largest element in the list.

li =[20,40,70,10,30,60]

max = li[0]
smax = 0

for i in range(0,len(li)):
    if(li[i] > max):
        smax = max
        max = li[i]
    elif(li[i] > smax):
        smax = li[i]


print(f'second Maximum element is {smax}')