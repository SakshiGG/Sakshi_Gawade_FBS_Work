# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

n = int(input('Enter number:'))

result = {}

x = 1
while (x <=n):
    result[x] = x *x
    x+=1

print(result)