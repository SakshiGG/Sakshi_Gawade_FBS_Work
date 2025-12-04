#WAP to check if given 3 digiit number is a palindrome or not.

num = int(input('Enter three-digit number:'))
temp = num

t1 = num % 10
num = num // 10

t2 = num % 10
num = num // 10

t3 = num % 10
num = num // 10

t1 *= 100
t2 *= 10

revNum = t3+t2+t1
print(revNum)

if(revNum == temp):
    print(f'{temp} is a palindrome')
else:
    print(f'{temp} is Not a palindrome')
