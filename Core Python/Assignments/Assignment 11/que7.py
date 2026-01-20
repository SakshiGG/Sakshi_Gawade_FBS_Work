# WAP to find intersection of two list.

def list_itersection(li1,li2):
    li3= []
    for elem in li1:
        if(elem in li2):
            li3.append(elem)

    return print('Intersection of two list:',li3)



li1 = [10,20,20,30,40,50]
li2 = [40,50,60,70,80]
list_itersection(li1,li2)