#WAP to input angles of a triangle and check whether triangle is valid or not

#Take input from user
a1 = int(input('Enter 1st angle of triangle:'))
a2 = int(input('Enter 2nd angle of triangle:'))
a3 = int(input('Enter 3rd angle of triangle:'))

#calculate angle
angle = a1 + a2 + a3

#check condition
if(angle > 180):
    print('Invalid Triangle')
else:
    print('Valid Triangle')