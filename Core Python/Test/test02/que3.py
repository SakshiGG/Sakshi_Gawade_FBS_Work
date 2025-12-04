# A farmer has a feild which is half in circle share and rest rectangle. 
# He needs to do fensing for entire feild using barbed wire 5 times.
# Circular section has radius 20m and rectangle length is 50m and breadth is 40m.
# If cost of barbed wire is 35Rs./m then calculate the total cost of fensing the feild.

radius = 20
length = 50
breadth = 40

#calculate perimeter of feild (rectangle + semi circle)
perimeter = (2*length)+breadth+(3.14*radius)

#Calculate wire required to fensing the feild 5 times
fensing = 5 * perimeter

#Total cost
cost = 35 * fensing

#Display Result
print(f'Total cost for fensing the feild is {cost}₹.')