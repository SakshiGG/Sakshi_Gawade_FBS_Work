# WAP to find the union of two list.


def list_union(li1,li2):
    union = []
    for elem in li1:
        if (elem not in union):
            union.append(elem)
        
    for elem in li2:
        if(elem not in union):
            union.append(elem)

    return print('Union of two list:',union)


li1 = [10,20,20,30,40,50]
li2 = [40,50,60,70,80]
list_union(li1,li2)

