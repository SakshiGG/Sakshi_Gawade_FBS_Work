# WAP to find sum of digits using recursion.


def digitSep(num):
    if(num == 0):
        return 0
    else:
        return num % 10 +digitSep(num//10)
    
n = int(input('Enter number:'))
print(digitSep(n))