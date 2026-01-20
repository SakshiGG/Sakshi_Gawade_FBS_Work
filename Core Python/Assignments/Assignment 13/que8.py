# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

text = 'apple banana apple apple mango orange cherry orange '

freq = {}

word = ''

for ch in text:
    if ch != ' ':
        word+=ch

    else:
        found = False
        for k in freq:
            if k == word:
                freq[k]=freq[k]+1
                found = True
                break
        if not found:
            freq[word] = 1

        word = ''

print(freq)