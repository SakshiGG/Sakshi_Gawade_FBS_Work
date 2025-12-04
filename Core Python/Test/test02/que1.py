#WAP to accept year from user and check if it is a leap year or not.

#Take year as a input from user 
year = int(input('Enter Year:'))

#check all conditions
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f'{year} is leap year.')
        else:
            print(f'{year} is not a leap year.')
    else:
        print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')