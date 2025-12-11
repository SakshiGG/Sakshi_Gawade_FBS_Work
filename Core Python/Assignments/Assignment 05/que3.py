# Accept no. of passengers from user and per ticket cost. 
# Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
#   a. Children below 12 = 30% discount
#   b. Senior citizen (above 59) = 50% discount
#   c. Others need to pay full.


num_passanger = int(input('Enter number of passangers:'))
cost = float(input('Enter ticket cost:'))

t_amount = 0
for i in range(1,num_passanger+1):
    age = int(input(f'Enter age of passanger {i}:'))

    if(age < 12):
        t_cost = cost - (cost * 0.30)
    elif(age > 59):
        t_cost = cost - (cost * 0.50)
    else:
        t_cost = cost

    t_amount = t_amount + t_cost

print(f'{t_amount}₹ is required to travel for {num_passanger} people.')

    