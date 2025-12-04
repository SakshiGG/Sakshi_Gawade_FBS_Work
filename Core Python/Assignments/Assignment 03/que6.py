#WAP to calculate profit or loss.

SP = float(input('Enter selling price:'))
CP = float(input('Enter cost price:'))

if(SP > CP):
    print('Profit')
elif(SP < CP):
    print('Loss')
else:
    print('No profit No loss')