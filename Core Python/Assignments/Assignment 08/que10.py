#WAP to check entered year is leap year or not.

def leapYear_orNot(year):
    if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

yr = int(input('Enter year to check:'))

if(leapYear_orNot(yr)):
    print(f'{yr} is leap year.')
else:
    print(f'{yr} is not a leap year.')
