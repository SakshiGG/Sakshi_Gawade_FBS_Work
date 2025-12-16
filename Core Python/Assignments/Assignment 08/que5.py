# Sum of all prime numbers between 1 to n.

def sum_prime(num):
    sum = 0
    for i in range(2,num+1):
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            sum += i
    return sum

n = int(input('Enter number:'))

print(sum_prime(n))


