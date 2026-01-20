# WAP to find second second large number in a list using bubble sort.

def bubble_sort(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0,size-1):
            if(li[j] > li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]

    return print('Second largest number is:',li[-2])



li = [80,20,15,75,61,3,78,19]
bubble_sort(li)
