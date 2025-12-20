# WAP to check whether given number is prime or not using recursion.

def prime(num,i=2):
    if(num <= 1):
        return False
    elif(i==n):
        return True
    elif(n%i==0):
        return False
    else:
        return prime(n,i+1)
    
def is_prime(num):
    if(prime(num)):
        print(f'{num} is prime number')
    else:
        print(f'{num} is not a prime number')


n = int(input('Enter number to check:'))
is_prime(n)