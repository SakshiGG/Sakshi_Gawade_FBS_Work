#WAP to calculate cost of painting the following building's walls(both nterior and exterior).You need to accept area(one wall) and cost of both interiorand exterior wall.
#Note: 1. given Diagram is of two joint room. 
# 2.It is upper view of building.


#Take input from user
area = int(input('Enter one wall area:'))
iCost = int(input('Enter cost for interior wall'))
eCost = int(input('Enter cost for exterior wall'))

#Calculate cost
extCost = 7 * eCost
intCost = 8 * iCost

#calculate total cost
cost = extCost + intCost 

#Display result
print(f'Total cost required to paint walls is {cost}₹.')





















