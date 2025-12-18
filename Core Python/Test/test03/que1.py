# WAP to print n prime numbers.

num = int(input('Enter Number:'))

count = 0
i = 2
while(count < num):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
        count+=1
    i+=1
