#WAP to print armstrong number within given range.  123


a = int(input('Enter start of range:'))
n = int(input('Enter end of range'))


for i in range(a,n+1):

    #count digits 
    temp = i
    count = 0
    while(temp > 0):
        temp //= 10
        count += 1

    #seperate digits and calculate sum and power
    temp = i
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp //= 10

    #power
        mult = 1
        for e in range(count):
            mult *= d
    #sum
        sum += mult

    if(sum == i):
        print(i, end =' ')
   


