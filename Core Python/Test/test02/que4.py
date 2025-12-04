#WAP to calculate the total cost of painting. The interior of building with four equal sized walls.

length = float(input('Enter length of wall:'))
breadth = float(input('Enter breadth of wall:'))
one_wall_cost = float(input('Enter cost to paint one wall:'))

area = 4* (length * breadth)

cost = one_wall_cost * area
print(f'{cost}₹ is required to paint interior of building.')


