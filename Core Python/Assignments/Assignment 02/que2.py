#WAP to convert temp from celsius to Fahrenheit. (C/5 = (F-32)/9)

#Take inputs from users
c = int(input('Enter temperature in celsius:'))

#convert celsius to fahrenheit
F = c * (9/5) + 32

#Display Result
print(f'{c} celcius into fahrenheit is {F}')

