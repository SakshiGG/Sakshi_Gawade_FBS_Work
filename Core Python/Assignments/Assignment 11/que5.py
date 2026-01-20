# WAP to sort a list according to the length of elements within the list.


words = ['computer','java','c','python']

def len_of_words(words):
    count = 0
    for i in words:
        count +=1

    return count

def sort_list(words):
    size = len(words)
    for i in range(1,size):
        for j in range(0,size - 1):
            if len_of_words(words[j]) > len_of_words(words[j+1]):
                words[j],words[j+1]=words[j+1],words[j]

    return print('Sorted list is:',words)


sort_list(words)