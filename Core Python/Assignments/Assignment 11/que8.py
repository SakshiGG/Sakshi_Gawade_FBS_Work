# Print 1 to 100 in snake and ladder pattern.

def snake_ladder_pattern():
    num = 1

    for row in range(10):
        if row % 2 == 0:
            for i in range(10):
                print(num,end=' ')
                num +=1

        else:
            temp = num + 9
            for i in range(10):
                print(temp,end=' ')
                temp -=1
            num +=10

        print()
    
snake_ladder_pattern()


