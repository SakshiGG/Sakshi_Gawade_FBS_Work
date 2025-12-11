#WAP to print following pattern.
#      1                           
#     1  1
#    1  2  1
#   1  3  3  1


n = int(input('Enter range:'))

for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')

    k = 1
    for j in range(1,i+1):
        print(k,end=' ')
        k = k*(i-j)//j

    print()


# 1
# 1 1
# 1 2 1
# 1 3 3 1