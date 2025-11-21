#WAP to convert days into years,weeks,days

#Take a Days from users
days = int(input("enter days:"))

#Calculate Year
years = days//365
remaining_days= days % 365


#Calculate weeks
weeks= remaining_days//7

#Calculate remaining days
days_left = remaining_days % 7

#Display result
print(f'Result: {years} years , {weeks} weeks , {days_left} days')