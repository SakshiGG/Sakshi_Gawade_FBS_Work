# WAP to check given number is armstrong or not using recursive function.



def countDigit(num):
    if(num==0):
        return 0
    else:                
        return 1 + countDigit(num//10)

def armstrong_sum(num,power):
    if(num==0):
        return 0
    d=num%10
    return (d**power)+armstrong_sum(num // 10,power)


def is_armstrong(num):
    power = countDigit(num)
    if(armstrong_sum(num,power)==n):
        print(f'{num} is armstrong number.')
    else:
        print(f'{num} is not armstrong number.')

n = int(input('Enter number to check:'))
is_armstrong(n)