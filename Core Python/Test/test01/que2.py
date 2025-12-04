#WAP to calculate simple interest based on principal,rate and time.

#Take inputs from user
P = int(input('Enter principal amount:'))
R = int(input('Enter Rate:'))
T = int(input('Enter Time in years:'))

#Claculate simple interest
SI = (P*R*T)/100

#Display simple interest
print(f'For principal amount:{P},Rate:{R},Time:{T} The simple interest is {SI}.')
