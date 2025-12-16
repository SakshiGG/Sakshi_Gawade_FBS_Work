#WAP to calculate ares of circle.

def area_circle(radius):
    return 3.14 * radius * radius

r = float(input('Enter radius of circle:'))

print(f'Area of circle is {area_circle(r)}')