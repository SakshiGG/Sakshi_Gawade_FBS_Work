#WAP to print all numbers in a range divisible by given number.

a = int(input('Enter start of range:'))
n = int(input('Enter end of range:'))

div = int(input('Enter divisor:'))

for i in range(a, n+1):
    if(i % div == 0):
        print(i)