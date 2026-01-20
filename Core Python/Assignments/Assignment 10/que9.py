# WAP of having n number of elements in the list and fibdout even and odd elements in that list 
# and then create two seperate list which will have even elements and other will have odd elements.


li = [1,2,3,4,5,6,7,8,9,10]

even_li=[]
odd_li=[]
for elem in li:
    if (elem%2==0):
        even_li.append(elem)
    else:
        odd_li.append(elem)

print('List of even elements:',even_li)
print('List of odd elements:',odd_li)
        