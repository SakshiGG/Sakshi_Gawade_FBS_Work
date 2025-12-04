#

#Take input from user
l= int(input('Enter length:'))
b= int(input('Enter breadth:'))
r= int(input('Enter radius:'))

#calculate area 
area = (l*b)+(0.5*3.14*r*r)

#calculate perimeter
perimeter = (l+l+b)+(3.14*r)

#Display result
print(f'Area of given diagram is {area}.')
print(f'Perimeter of given diagram is {perimeter}.')