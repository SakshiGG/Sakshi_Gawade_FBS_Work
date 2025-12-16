# WAP to find print the following fibonacci series using function:
# 1 1 2 3 5 8...n

def fibonacci_series(num):
    a,b=1,0

    for i in range(num):
        c=a+b
        a=b
        b=c

    return c

n = int(input('Enter number:'))
print(fibonacci_series(n))