#WAP to check given number is perfect number.        6 = 1 + 2 + 3


num = int(input('Enter number:'))
sum = 0

for i in range(1,num):  # 1 2 3 4 5  
    if(num % i == 0):      # 6%1=0   # 6%2=0 # 6%3=0 # 6%4=2 # 6%5=1
        sum = sum + i       # 0+1=1   # 1+2=3 # 3+3=6  
        
if(num == sum):
    print(f'{num} is perfect number.')
else:
    print(f'{num} is not a perfect number.')

