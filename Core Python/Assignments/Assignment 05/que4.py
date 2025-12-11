# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)


num = int(input('Enter any number to check:'))
temp = num

count = 0
while(temp > 0):
    temp//= 10
    count+=1

temp = num
sum = 0

while(temp>0):
    d = temp % 10             

    mult = 1
    for i in range(1,count+1):     
        mult = d * mult

    sum = sum + mult
    temp//=10

print(sum)

if(sum == num):
    print(f'{num} is armstrong number.')
else:
    print(f'{num} is not a armstrong number.')
