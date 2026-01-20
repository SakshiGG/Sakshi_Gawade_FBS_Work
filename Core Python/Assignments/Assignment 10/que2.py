# WAP to find maximum and minimum from list

li =[20,40,70,10,30,60]

max = li[0]
for i in range(0,len(li)):
    if(li[i] > max):
        max = li[i]

print(f'Maximum number is {max}')


min = li[0]
for i in range(0,len(li)):
    if(li[i] < min):
        min = li[i]

print(f'Minimum number is {min}')