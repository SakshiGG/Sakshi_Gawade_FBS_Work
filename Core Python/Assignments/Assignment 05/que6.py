# Write a program to print first n prime numbers.

num = int(input('Enter how many prime numbers you want:')) #5    #2 3 5 7 11

count = 0
i = 2
while(count < num):         

    for j in range(2,i):
        if(i % j == 0):
            break   
    else:
        print(i)
        count += 1
    i += 1