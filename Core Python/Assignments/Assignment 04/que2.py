#WAP to print odd number until n.

n = int(input('Enter range:'))

#METHOD 01
for i in range(1, n+1 , 2):
    print(i)

#METHOD 02
for i in range(1, n+1):
    if(i % 2 !=0):
        print(i)
