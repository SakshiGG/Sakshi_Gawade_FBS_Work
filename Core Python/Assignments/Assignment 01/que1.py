#WAP to calculate percentage of a student in 5 subjects.

#Take user input
Maths = int(input('enter Maths marks:'))
Science = int(input('enter Science marks:'))
History = int(input('enter History marks:'))
English = int(input('enter English marks:'))
Marathi = int(input('enter Marathi marks:'))

#Calculate total marks 
total_marks = Maths + Science+ History+ English+ Marathi

#Calculate percentage
percent=(total_marks/500) * 100

#Display Result
print('Percentage:', percent)