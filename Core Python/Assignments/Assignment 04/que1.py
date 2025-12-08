#WAP to print even numbers until n.

n = int(input('Enter number:'))

#METHOD 01
for i in range(2, n+1 , 2):
    print(i)

#METHOD 02
for i in range(2, n+1):
    if(i % 2 == 0):
        print(i)