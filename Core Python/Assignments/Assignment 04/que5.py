#WAP to print fibonacci series upto n.
# 0 1 1 2 3 5 8 13 21

num = int(input('Enter number you want to print from fibonacco series: '))
a , b = -1 , 1

for i in range(num):
    c = a+b
    a = b
    b = c
    print(c)



