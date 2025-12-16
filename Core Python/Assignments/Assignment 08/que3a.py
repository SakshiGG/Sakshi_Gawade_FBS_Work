# WAP to find sum of following series using function.
# a. 1+2+3+4+5+6......+n

def sum_series(num):
    sum = 0
    for i in range(1,num+1):
        sum += i

    return sum

n = int(input('Enter number:'))

print(sum_series(n))