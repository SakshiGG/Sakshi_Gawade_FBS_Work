# Input 5 subject marks from user and display grade(first class,second class,....)
# < 35 - failed
# > 65 - second class
# > 85 - first class
# > 35 - Third Division

sub1 = int(input('Enter sub1 marks:'))
sub2 = int(input('Enter sub2 marks:'))
sub3 = int(input('Enter sub3 marks:'))
sub4 = int(input('Enter sub4 marks:'))
sub5 = int(input('Enter sub5 marks:'))

marks = sub1 + sub1 + sub3 + sub4 + sub5

percent = (marks/500) * 100


if(percent < 35):
    print("Failed")
else:
    if(percent > 70):
        if(percent > 85):
            print("First Class")
        else:
            print("Second class")
    else:
        print("Third Division")

    