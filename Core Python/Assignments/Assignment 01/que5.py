#WAP to enter P,T,R and Calculate compound Interest

#Take input from user
P = float(input("Enter Principal Amount (P): "))
T = float(input("Enter Time (T) in years: "))
R = float(input("Enter Rate of Interest (R): "))

#Calculate Compound Interest
CI = P * ( (1 + R/100) ** T ) - P

#Display result
print("Compound Interest (CI):", CI)    