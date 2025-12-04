# WAP to accept 3 digit number. If first digit is double of second digit and half of third digit
# then display "Yes, you have done it",otherewise display "Please try Next time."

#Take three digit number as a input from user
num = int(input('Enter three-digit number:'))


n3 = num % 10
num = num // 10

n2 = num % 10
num = num // 10

n1 = num % 10
num = num // 10



if(n1 == 2*n2):
    if(n1 == n3/2):
        print('Yes, you have done it')
    else:
        print('Try again next time')
else:
    print('Try again next time')

