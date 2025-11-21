###Identity operator
x = 10                              #immutable value
y = 10
li1 = [10,20,30]                     #mutable value
li2 = [10,20,30]

#1. is
print(id(x))                 #checks memory address of x
print(id(y) )                #checks memory address of y
print(x is y)

print(id(li1))                 #checks memory address of li1
print(id(li2))                 #checks memory address of li2
print(li1 is li2)


#2. is not
print(li1 is not li2)