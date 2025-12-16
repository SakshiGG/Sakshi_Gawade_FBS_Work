#WAP to calculate area of rectangle.

def area_rect(length,breadth):
    return length * breadth

l=float(input('Enter length of rectangle:'))
b=float(input('Enter breadth of rectangle:'))

print(f'area of rectangle is {area_rect(l,b)}')
