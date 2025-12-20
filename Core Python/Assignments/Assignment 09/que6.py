# WAP to print fibonacci series using recursion.


def fibo(a,b,n):
    if(n!=0):
        c=a+b
        print(c)
        fibo(b,c,n-1)

a= -1
b= 1
n = int(input('Enter range:'))
fibo(a,b,n)




    




