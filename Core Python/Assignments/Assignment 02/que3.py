#WAP to convert distants given in feet and inches into meter and centimeter.

#Take inputs from user
feet = int(input('enter feet value:'))
inches = int(input('enter inches value:'))

#convert feet into inches
total_inches = feet * 12 + inches

#convert inches into meter and centimeter
meter = total_inches * 0.0254
cm = total_inches * 2.54

#display result
print(f'{feet}feet & {inches}inches in meter is {meter}m and in centimeter is {cm}cm.')