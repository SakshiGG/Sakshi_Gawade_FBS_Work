#WAP to find sum of digits of number.

def sum_digit(num):
    temp = num
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp //=10

        sum += d

    return sum

n = int(input('Enter number:'))
print(sum_digit(n))
