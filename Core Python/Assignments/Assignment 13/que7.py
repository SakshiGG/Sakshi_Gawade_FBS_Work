# Python Program to Remove the Given Key from a Dictionary.

d = {'a':1,'b':2,'c':3,'d':4,'e':5}
new_d = {}

key = input('Enter key to remove:')

for k in d:
    if (key != k):
        new_d[k] = d[k]

d = new_d
print(d)