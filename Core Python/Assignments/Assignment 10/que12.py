# WAP to create three list of numbers ,their cubes and squares.

num = [2,3,4,5]

n = []
sqr = []
cubes = []
for elem in num:
    n.append(elem)
    sqr.append(elem ** 2)
    cubes.append(elem ** 3)

print(n)
print(sqr)
print(cubes)
