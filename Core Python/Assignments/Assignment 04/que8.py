#WAP to find which number are divisible by 7 and multiple of 5 in given range.

a = int(input('Enter start of range:'))
n = int(input('Enter end of range:'))

for i in range(a, n+1):
    if(i % 7 == 0 and i % 5 ==0):
        print(i)