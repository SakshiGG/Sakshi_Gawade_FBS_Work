#WAP to reverse three-digit number.

#Take input from user
num = int(input('Enter three digit number:')) 
temp = num   #348

#Seperate digits
d1 = num % 10               # 348 % 10 = 8
num = num // 10             # 348 // 10 = 34

d2 = num % 10               # 34 % 10 = 4
num = num // 10             # 34 // 10 = 3

d3 = num % 10               # 3 % 10 = 3
num = num // 10             # 3 // 10 = 0

#Reverse digit
d1 = d1 * 100               # 8 * 100 = 800
d2 = d2 * 10                # 4 * 10 = 40

#Final Digit
num = d1 + d2 + d3          # 800 + 40 + 3 = 843

#Display Result
print(f'Reverse number of {temp} is {num}')


