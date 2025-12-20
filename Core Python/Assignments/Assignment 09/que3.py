# WAP to reverse a given number using recursive function.

def revrese(n,rev=0):
    if(n==0):
        return rev
    else:
        return revrese(n//10,rev*10 + n%10)
    

n = int(input('Enter number to reverse:'))
print(revrese(n))