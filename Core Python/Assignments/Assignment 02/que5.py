#WAP to calculate selling price of book based on cost price and discount.

#Take input from user
cp = int(input('Enter Cost price:'))
discount = int(input('Enter Discount in percentage:'))

#Calculate percentage amount
amount = cp * (discount/100)

#Calculate selling price 
sp = cp - amount

#Display result
print(f'Selling price is {sp}')
