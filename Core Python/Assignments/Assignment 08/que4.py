# Sum of all odd numbers between 1 to n.
    
#METHOD 1
def odd_sum(num):
    sum = 0
    for i in range(1,num+1):
        if(i%2!=0):
            sum += i
    return sum
    
n = int(input('Enter number:'))
print(odd_sum(n))



# METHOD 2
# def odd_sum(num):
#     sum = 0
#     for i in range(1,num+1,2):
#         sum += i
#     return sum
    
# n = int(input('Enter number:'))
# print(odd_sum(n))



