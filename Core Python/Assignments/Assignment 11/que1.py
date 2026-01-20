# WAP to put even and odd elements of list into two different lists.

def even_odd(li):

    even =[]
    odd = []
    for elem in li:
        if(elem % 2 == 0):
            even.append(elem)
        else:
            odd.append(elem)

    print('Even list:',even)
    print('Odd List:',odd)


li = [1,2,3,4,5,6,7,8,9,10]
even_odd(li)
