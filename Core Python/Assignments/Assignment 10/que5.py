# Accept number from user and check if this element is present in the list or not. 
# also tell how many times it is present in the list.

n = int(input('Enter number:'))

li =[20,40,70,10,30,60,10]

count = 0
for ele in li:
    if(ele == n):
        count+=1


if(count>=1):
    print(f'{n} is present in the list {count} times.')    
else:
    print(f'{n} is not present in the list.') 




