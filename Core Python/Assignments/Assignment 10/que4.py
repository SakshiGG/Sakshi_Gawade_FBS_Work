# WAP to reverse the list.

li =[20,40,70,10,30,60]

start = 0
end = len(li) - 1


while(start < end):
    li[start],li[end] = li[end],li[start]

    start += 1
    end -= 1

print(li)
