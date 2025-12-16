# WAP to check if entered number is a palindrome or not.

def reverse(num):
    rev = 0
    while(num > 0):
        rev = rev * 10 + num % 10
        num //= 10

    return rev

def palindrome_orNot(num):
    if(reverse(n) == num):
        return True
    else:
        return False
    
# def palindrome_orNot(num):
#     return reverse(n) == num
    
n = int(input('Enter number:'))

if(palindrome_orNot(n)):
    print(f'{n} is palindrome')
else:
    print(f'{n} is not a palindrome')
