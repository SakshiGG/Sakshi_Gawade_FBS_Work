# Write a program to prompt user to enter userid and password.
# If id and password is incorrect give him chance to re-enter the credentials.
# Let him try 3 times . after that, program to terminate.

userId = 'Admin'
passw = 'Admin@123'

uId = input('Enter User ID:')
pwd = input('Enter password:')

if(userId == uId and passw == pwd):
    print('Login Successful')
else:
    for i in range(3):
        print('--Invalid Credentials--')
        print('--Try Again--')
        uId = input('Enter User ID:')
        pwd = input('Enter password:')
        if(userId == uId and passw == pwd):
            print('Login Successful')
            break

    else:
        print('--INVALID LOGIN CREDENTIALS--')
        print('--Thanks for visiting--')






    

