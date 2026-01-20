# WAP to sort the list according to the second element in sublist.

def selectionSort(li):
    size = len(li)
    for i in range(0,size-1):
        min = i
        for j in range(i+1,size):
            if(li[min][1] > li[j][1]):
                min = j
            li[min],li[i] = li[i],li[min]



li = [[10,5],[30,7],[20,3],[50,2]]
print('Before sorting',li)
selectionSort(li)
print('After sorting',li)
