#WAP to accept distance in km and convert it into meters and centimeter both.

#Take input from user
km = int(input('Enter Distance in kilometer:'))

#Convert kilometer into meter
meter = km * 1000

#Convert kilometer into centimeter
cm = km * 1000 * 100

#Display result
print(f'{km}km in meter is {meter}m and in centimeter is {cm}cm.')
