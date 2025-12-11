# Enter number of students from user. 
# For those many students accept marks of 5 subject marks from user and calculate percentage. 
# Display all percentage and average percentage of students.

studentNum = int(input('Enter number of students:'))

avg = 0
for i in range(1,studentNum+1):
    print(f'Enter marks of 5 subject for student {i}:')
    s1 = float(input('subject 1:'))
    s2 = float(input('subject 2:'))
    s3 = float(input('subject 3:'))
    s4 = float(input('subject 4:'))
    s5 = float(input('subject 5:'))

    sum = s1 + s2 + s3 + s4 + s5
    perc = (sum / 500 ) * 100
    print(f'Prcentage of student {i} is {perc}%.')

    avg = (perc + avg)/studentNum

print(f'average is {avg}%.')



