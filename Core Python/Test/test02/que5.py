# A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST.

p1 = float(input('Enter cost of 1st product.'))
p2 = float(input('Enter cost of 2nd product.'))
p3 = float(input('Enter cost of 3rd product.'))
p4 = float(input('Enter cost of 4th product.'))
p5 = float(input('Enter cost of 5th product.'))

cost = p1 + p2 + p3 + p4 + p5

gst = cost * (18/100)

total_cost = cost + gst

print(f'Total bill with 18% GST is {total_cost}₹.')