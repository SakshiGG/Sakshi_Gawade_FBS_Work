# WAP to print following pattern.
#         1 
#       1 2 3 
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9

for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')

    for j in range(1,i+1):
        print(j,end=' ')
    k = 1
    for j in range(1,i):
        print(k+i,end=' ')
        k+=1
    print()