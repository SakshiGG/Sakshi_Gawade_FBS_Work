#WAP to calculate sum of three digit number.

#Take input
num = int(input("Enter three-digit number:"))
temp = num

#Seperate digits
d1 = num % 10               #348 % 10 = 8
num = num // 10             #348 // 10 = 34

d2 = num % 10               #34 % 10 = 4
num = num // 10             #34 // 10 = 3

d3 = num % 10               #3 % 10 = 3
num = num // 10             #3 // 10 = 0

#Addition of digits
sum = d1+d2+d3              #8+4+3 = 15

#Display result
print(f'Addition of {temp} digit is {sum}.')