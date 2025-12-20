# WAP to calculate m to the power n using recursion.

def power(m,n):
    if(n==0):
        return 1
    else:
        return m * power(m,n-1)
    

m = int(input('Enter base number:'))
n = int(input('Enter power number:'))
print(power(m,n))