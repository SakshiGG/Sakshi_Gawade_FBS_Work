#WAP to print factorial of number.

num = int(input('Enter number:'))
fact = 1

#for i in range(1,num+1):
for i in range(num ,0,-1):
    fact = i * fact
print(f'Factorial of {num} is {fact}.')


