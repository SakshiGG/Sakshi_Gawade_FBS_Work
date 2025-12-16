# WAP to find sum of following series using function.
# a. 1^1 + 2^2 + 3^3 +.......+n^n

def expo_sum(num):
    sum =0
    for i in range(1,num+1):
        sum = sum + (i ** i)
    return sum

n = int(input('Enter number:'))
print(expo_sum(n))
