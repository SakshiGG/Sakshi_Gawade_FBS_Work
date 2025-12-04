# WAP to prompt user to enter userid and password.
# After verifying userid and password display a 4 digit random number and ask user to enter the same.
# If user enters the same number then show him success message otherwise failed.

import random

correct_userId = 'Admin'
correct_pw = 'Admin@123'
random_code = random.randint(1000 , 9999)

userId = input('Enter user ID:')
password = input('Enter password:')

if(correct_userId == userId):
    if(correct_pw == password):
        print(f'Random code: {random_code}')
        code = int(input('Enter random code here:'))
        if(random_code == code):
            print('Login Successful')
        else:
            print('Login Failed')
    else:
        print('Invalid UserId or Password')
else:
    print('Invalid UserId or Password')



