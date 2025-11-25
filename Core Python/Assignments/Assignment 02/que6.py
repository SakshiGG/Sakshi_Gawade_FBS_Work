#WAP to calculate total salary of employee based on basic , da = 10% of basic,ta = 12% of basic, hra=15% of basic.

#Take input from users.
salary = int(input('Enter salary of employee:'))

#calculate da,ta,hra
da = salary * (10/100)

ta = salary * (12/100)

hra = salary * (15/100)

#Calculate total salary
total_salary = salary + da + ta + hra

#Display Result
print(f'Total salary of employee is {total_salary}')


