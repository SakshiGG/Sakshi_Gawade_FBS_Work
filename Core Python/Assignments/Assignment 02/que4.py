#WAP to calculate area of triangle and rectangle


#Area of triangle
base = int(input('Enter Base of triangle:'))
height = int(input('Enter height of triangle:'))

#Calculate area of triangle
area_tri = (1/2)*base*height

#Display result
print(f'Area of triangle is {area_tri}')

#Area of Rectangle
length = int(input('Enter length of Rectangle:'))
width = int(input('Enter width of Rectangle:'))

#Calculate area of Rectangle
area_rect = length * width


print(f'Area of rectangle is {area_rect}')
