# Accept age of five people and also per person ticket amount. 
# and then calculate total amount to ticket to travel for all of them based on follwing condition:
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. other need to pay full.


# age of five people as input
p1 = int(input('Enter age of 1st person:'))             # 8 child
p2 = int(input('Enter age of 2nd person:'))             # 35 adult
p3 = int(input('Enter age of 3rd person:'))             # 62 senior
p4 = int(input('Enter age of 4th person:'))             # 10 child
p5 = int(input('Enter age of 5th person:'))             # 59 adult

# amount of ticket
amt = int(input('Enter ticket amount:'))                # 100

# condition for 1st person 
if(p1 < 12):                             # 8 < 12 child
    amt1  = amt - (amt * (30/100))       # 100 * (30/100) 
elif(p1 > 59):                           # amt1 = 70
    amt1  = amt - (amt * (50/100))
else:
    amt1 = amt

# condition for 2nd person 
if(p2 < 12):
    amt2 = amt - (amt * (30/100))
elif(p2 > 59):      
    amt2 = amt - (amt * (50/100))
else:                                    # 35 adult
    amt2 = amt                           # amt2 = 100

# condition for 3rd person 
if(p3 < 12):
    amt3 = amt - (amt * (30/100))
elif(p3 > 59):                           # 62 > 59 senior
    amt3 = amt - (amt * (50/100))        # 100 * (50/100)
else:                                    # amt3 = 50
    amt3 = amt

# condition for 4th person 
if(p4 < 12):                             # 10 < 12 child
    amt4 = amt - (amt * (30/100))        # 100 * (30/100)
elif(p4 > 59):                           # amt4 = 70
    amt4 = amt - (amt * (50/100))
else:
    amt4 = amt

# condition for 5th person 
if(p5 < 12):                             
    amt5 = amt - (amt * (30/100))
elif(p5 > 59):
    amt5 = amt - (amt * (50/100))
else:                                    # 59 adult
    amt5 = amt                           # amt5 = 100

total_amount = amt1 + amt2 + amt3 + amt4 + amt5        # 70 + 100 + 50 + 70 + 100

print(f'Total amount for ticket {total_amount}₹.')