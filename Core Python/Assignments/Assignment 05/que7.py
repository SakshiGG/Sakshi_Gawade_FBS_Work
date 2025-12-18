# Write a program to solve the following series :

# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
ch = 0
while(ch!='f'):
    print('a. 1! + 2! + 3! + 4! + .....n!')
    print('b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)')
    print('c. Find the sum of a geometric series from 1 to n where the common ratio is 2.')
    print('d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10')
    print('e. x - x2/3 + x3/5 - x4/7 + .... to n terms')
    print('f.EXIT')
    print('--------------------')

    ch = input('Enter your choise:')

    if(ch == 'a'):
        print('--------- 1! + 2! + 3! + 4! + .....n! ---------')
        r = int(input('Enter range upto you want to calculate the series:'))
        fact = 1
        sum = 0
        for i in range(1,r+1):
            fact = fact * i
            sum += fact
        print(f'Sum of Factorials upto {r} is {sum}.')
        print('-------------------------------')

    elif(ch == 'b'):
        print('--------- N + N^2 + N^3+N^4 .....+N^N ---------')
        sum = 0
        r = int(input('Enter range upto you want to calculate the series:')) 
        for i in range(1,r+1):
            expo = r ** i
            sum = sum + expo
        print(f'sum of Exponential of series upto {r} is {sum}')
        print('-------------------------------')

    elif(ch == 'c'):
        print('--------- sum of a geometric series from 1 to n where the common ratio is 2. --------')
        
        n = int(input('enter range:'))
        num = 1
        sum = 0
        for i in range(n):
            sum += num
            num *=2 
        print(f'Sum of a geometric series from 1 to {n} is {sum}.')
        print('-------------------------------')

    elif(ch == 'd'):
        print('-------- S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10 --------')
        sum = 0
        a = int(input('Enter number:'))
        for i in range(1,11):
            div = (a*i)/ i
            sum = sum + div
        print(f'S = {sum}')
        print('-------------------------------')

    elif(ch == 'e'):
        print('-------- x - x2/3 + x3/5 - x4/7 + .... to n terms ---------')

        n = int(input('Enter range:'))
        x = float(input('Enter value of x:'))

        sum = 0  
        k = 1
        sign = 1

        for i in range(1,n+1):
            term = sign * (x * i)/k
            k+=2
            sum = term + sum

            sign *= -1

        print(f'Answer: {sum}')
        print('-------------------------------')
    
    elif(ch=='f'):
        print('Thanku for visiting.')
        print('-------------------------------')

    else:
        print('INVALID CHOISE.')
        print('-------------------------------')
    


