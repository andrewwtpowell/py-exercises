def pyramid(height):

    if height < 1:
        print('Invalid input: height must be greater than 0')
        return None

    for i in range(1,height+1):
        row = ' '*(height-i) + '#'*(i*2-1) + ' '*(height-i)
        print(row)


pyramid(10)
pyramid(5)
pyramid(3)
pyramid(1)
pyramid(15)
