#WAP to enter P,T,R and calculate Simple Interest

#Take input from user
P = float(input("Enter Principal Amount (P): "))
T = float(input("Enter Time (T) in years: "))
R = float(input("Enter Rate of Interest (R): "))

#Calculate Simple Interest
SI = (P * T * R) / 100

#Display result
print("Simple Interest (SI):", SI)