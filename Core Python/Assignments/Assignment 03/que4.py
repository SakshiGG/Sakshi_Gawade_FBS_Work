#WAP to input all sides of triangle and check whether triangle is valid or not.

#Enter input
s1 = int(input('Enter 1st side of triangle:'))
s2 = int(input('Enter 2nd side of triangle:'))
s3 = int(input('Enter 3rd side of triangle:'))

#METHOD 01
if(s1+s2 >s3):
    if(s2+s3 >s1):
        if(s3+s1 > s2):
            print('Valid triangle')
else:
    print('Invalid triangle')

#METHOD 02

#   if((s1+s2 > s3) and (s2+s3 >s1) and (s3+s1 > s2)):
#       print('Valid Triangle')
#   else:
#       print('not valid')
