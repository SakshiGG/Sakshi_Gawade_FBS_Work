# WAP to calculate the sum of following series. where n is input by user.
# 1/1! + 2/2! + 3/3! +.......+n/n!

n = int(input('Enter number:'))

fact = 1
sum = 0
for i in range(1,n+1):
    fact = fact * i

    series = i/fact
    sum += series

print(f'Sum of given series is {sum}')
