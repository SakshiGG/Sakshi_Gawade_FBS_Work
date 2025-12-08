#WAP to check given number is strong number.  145 = 1! + 4! + 5!


num = int(input('Enter number:'))
temp = num
sum = 0
while(num > 0):                    
    d = num % 10                   
    #print(d)
    num = num // 10   
    #print(num)  
    fact = 1    
    for i in range(1,d+1):        
        #print(i, end = ' ')
        fact = i * fact            
        #print(f'{fact} * {i} ', end = ' ')
    #print(fact)
    sum = fact + sum               
#print(sum)
 

if(sum == temp):
    print(f'{temp} strong number.')
else:
    print(f'{temp} not a strong number.')
