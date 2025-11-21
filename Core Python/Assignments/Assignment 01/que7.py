#WAP to find roots of quadratic equation

#Take input
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

#Calculate roots of quadratic equation

val = (b**2) - 4*a*c                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

root1 = (-b + val** 0.5)/2*a
root2 = (-b - val** 0.5)/2*a


#Display result
print("Root 1 is", root1)
print("Root 2 is", root2)