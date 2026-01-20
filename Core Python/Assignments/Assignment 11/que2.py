# WAP to merge and sort it.

def merge_and_sort(li1,li2):
    merge = []
    for elem in li1:
        merge.append(elem)

    for elem in li2:
        merge.append(elem)

# Bubble sort
    size = len(merge)
    for i in range(1,size):
        for j in range(0,size - i):
            if(merge[j] > merge[j + 1]):
                merge[j],merge[j+1] = merge[j+1],merge[j]

    return merge

li1=[80,20,15,75]
li2=[61,3,78,19]
merge = []
res = merge_and_sort(li1,li2)
print(res)