#WAP to check whether the triangle is equilateral , isoscales or scalene triangle.
#equilateral - all three sides are equal in length
#isoscales - exactly two sides are equal in length
#scalene - all three sides are different


#Take inputs from user
s1 = int(input('Enter 1st side of triangle:'))
s2 = int(input('Enter 2nd side of triangle:'))
s3 = int(input('Enter 3rd side of triangle:'))


if(s1 == s2 == s3):
    print('Equilateral triangle')               
elif(s1 == s2 or s2 == s3 or s1 == s3):
    print('Isoscalen Triangle')
else:
    print('Scalene triangle')
