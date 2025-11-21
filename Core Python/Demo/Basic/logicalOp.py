####Logical
#1. and: Return True if both operands are True, otherwise False
print(True and True)
print(True and False)

#2. or: Return False if both operands are False, otherwise True
print(False or False)
print(False or True)

#3. not: Return opposite result
print(not True)
print(not False)


# op1 | op2 | and | or
# T   |  T  |  T  | T
# T   |  F  |  F  | T
# F   |  T  |  F  | T
# F   |  F  |  F  | F


#Note: Falsy value: zero or null
#0, None, False, '', [],
#Other values are Truely values