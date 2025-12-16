# WAP to find reverse of number.

def reverse(num):
    rev = 0
    while(num > 0):
        rev = rev * 10 + num % 10 
        num //= 10

    return rev

n = int(input('Enter number:')) 
print(reverse(n))

