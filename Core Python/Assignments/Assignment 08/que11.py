# WAP to check if a given number is armstrong number or not.
# for each task create seperate function.

def count_digit(num):
    temp = num
    count = 0
    while(temp > 0):
        temp //=10
        count+=1
    return count

def armstrong_num(num):
    count = count_digit(num)
    temp = num 
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp//=10

        mult = 1
        for i in range(1,count+1):
            mult *= d

        sum += mult
    return sum

n = int(input('Enter number:'))
if(armstrong_num(n) == n):
    print(f'{n} is armstrong number.')
else:
    print(f'{n} is not a armstrong number.')
