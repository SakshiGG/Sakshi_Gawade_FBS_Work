#WAP to swap two numbers using third variable.

#Take input from the user
x = int(input('Enter first number (x): '))
y = int(input('Enter second number (y): '))

#Display numbers before swapping
print(f'Before swapping: x = {x}, y = {y}')

#Swap the numbers using a third variable
temp = x 
x = y
y = temp

#Display numbers after swapping
print(f'After swapping: x = {x}, y = {y}')