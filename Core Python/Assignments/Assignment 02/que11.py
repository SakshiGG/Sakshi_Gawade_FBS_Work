#WAP to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

#Take input from user
amt = int(input('Enter amount:'))            #4880
amount = amt

#find notes required 
t1 = amt // 2000                        # 4880 // 2000 = 2
amt = amt % 2000                        # 4880 % 2000 = 880

t2 = amt // 500                         # 880 // 500 = 1
amt = amt % 500                         # 880 % 500 = 380

t3 = amt // 200                         # 380 // 200 = 1
amt = amt % 200                         # 380 % 200 = 180

t4 = amt // 100                         # 180 // 100 = 1
amt = amt % 100                         # 180 % 100 = 80

t5 = amt // 50                          # 80 // 50 = 1
amt = amt % 50                          # 80 % 50 = 30

t6 = amt // 20                          # 30 // 20 = 1
amt = amt % 20                          # 30 % 20 = 10

t7 = amt // 10                          # 10 // 10 = 1
amt = amt % 10                          # 10 % 10 = 0

notes = t1 + t2 + t3 + t4 + t5 + t6 + t7               # 2 + 1 + 1 + 1 + 1 + 1 + 1 = 8

print(f'total number of notes required to represent {amount} is {notes} notes.')       # 8 notes will required to represent 4880₹