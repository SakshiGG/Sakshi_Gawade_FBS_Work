#WAP to check if person is eligible to marry or not(male age>=21 and female age>=18)

age = int(input('Enter age:'))
gender = input('Enter Gender (M/F):')

if(gender == 'M'):
    if(age >=21):
        print('Eligible for marraige (Male).')
    else:
        print('Not Eligible for marraige (Male).')
else:
    if(age >=18):
        print('Eligible for marraige (Female).')
    else:
        print('Not Eligible for marraige (Female).')