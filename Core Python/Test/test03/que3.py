# WAP to accept basic salary of n emp.(n should be accepted from user).
# If basic salary is below 20000 then da=10%,ta=12%, and hra=15%
# otherwise da=15%,ta=18% and hra=20%
# Base on this calculate total salary of all emp

n = int(input('Enter number of employees:'))

total_salary = 0
for i in range(1,n+1):
    slr = int(input(f'Enter basic salary of emp{i}:'))

    if(slr < 20000):
        da = slr * 0.10
        ta = slr * 0.12
        hra = slr * 0.15
    else:
        da = slr * 0.15
        ta = slr * 0.18
        hra = slr * 0.20

    salary = slr + da + ta + hra

    total_salary += salary 

print(f'Total Salary of {n} employees is {total_salary}₹.')

