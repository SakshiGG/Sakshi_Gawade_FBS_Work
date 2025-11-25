#WAP to swap two numbers without using third variable


#Take input from user
x = int(input('Enter number:'))  #20
y = int(input('Enter number:'))  #10

#Display numbers before swapping
print(f'Before swapping: x = {x}, y = {y}')         # x = 20 , y = 10

#MTHOD 01
x = x + y                 #20 + 10 = 30
y = x - y                 #30 - 10 = 20
x = x - y                 #30 - 20 = 10

#Display numbers before swapping
print(f'After swapping: x = {x}, y = {y}')          # x = 10 , y = 20


#MTHOD 02
x,y = y,x

#Display numbers before swapping
print(f'After swapping: x = {x}, y = {y}')         # x = 20 , y = 10