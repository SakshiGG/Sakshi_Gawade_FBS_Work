#WAP to check number is positive or negative or neutral

#Take input from user
num = int(input("Enter number to check pos or neg:"))

#check conditions
if(num == 0):
    print(f'{num} is neutral number.')
elif(num > 0):
    print(f'{num} is positive number.')
else:
    print(f'{num} is negative number.')