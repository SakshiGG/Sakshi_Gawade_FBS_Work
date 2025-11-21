#WAP to input two angles from users and find the third angle of triangle.

#Take Inputs from users
angle1 = int(input("enter angle 1:"))
angle2 = int(input("enter angle 2:"))

#calculate third angle
angle3 = 180 - (angle1 + angle2)

#Display Result
print("Valur of third angle is", angle3)