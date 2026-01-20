# Python Program to Check if a Given Key Exists in a Dictionary or Not.

d1 = {'Python':1,'SQL':2,'Data Science':3,'java':4}
key = input('Enter key:')

found = False
for k in d1:
    if(key == k):
        found = True
        break

if(found):
    print('Key exist')
else:
    print('Key does not exist')
