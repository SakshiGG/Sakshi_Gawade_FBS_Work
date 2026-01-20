# Python Program to Multiply All the Items in a Dictionary.

d = {'a':1,'b':2,'c':3,'d':4,'e':5}

mult = 1
for k in d:
    mult *= d[k]

print(mult)