# WAP to input electricity unit charges and calculate total electricity bill according to given condition :
# For first 50 units RS. 0.50/unit.
# For next 100 units RS. 0.75/unit.
# For next 100 units RS. 1.20/unit.
# For unit above 250 RS. 1.50/unit.
# An additional surcharge of 20% is added to the bill.

# METHOD 01 (Using if-else ladder)

units = float(input('Enter electricity units:'))

if(units <= 50):
    bill = units * 0.50
elif(units <= 150):
    bill = (50 * 0.50) + ((units - 50) * 0.75)
elif(units <= 250):
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 150) * 1.50)

T_bill = bill + (bill * (20/100))

print(f'Total electricity bill is {T_bill}.')




# METHOD 02 (Using Nested if-else)

#units = float(input('Enter electricity units:'))

#if(units <= 250):
#    if(units <= 150):
#        if(units <= 50):
#            bill = units * 0.50
#        else:
#            bill = (50 * 0.50) + ((units - 50) * 0.75)
#    else:
#        bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
#else:
#    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 150) * 1.50)


#T_bill = bill + (bill * (20/100))

#print(f'Total electricity bill is {T_bill}.')


