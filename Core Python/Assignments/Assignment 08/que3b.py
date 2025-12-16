# WAP to find sum of following series using function.
# a. 1! + 2! + 3! + 4! +......+ n!


def factorial(num):
    mult = 1
    sum = 0
    for i in range(1,num+1):
        mult = i * mult
    
    sum += mult

    return sum

n = int(input('Enter number:'))

print(factorial(n))