#WAP to check if user has entered correct userid and password.

correct_userId = 'Admin'
correct_pw = 'Admin@123'

userId = input('Enter user ID:')
password = input('Enter password:')

if(correct_userId == userId):
    if(correct_pw == password):
        print('Login Successful')
    else:
        print('Invalid UserId or Password')
else:
    print('Invalid UserId or Password')
