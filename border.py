def border(width, height):

    if width < 2 or height < 2:
        print('Invalid input: must enter width and height larger than 2')
        return None
    
    corner = '+'
    horiz_border = '-'
    vert_border = '|'

    outer_row = corner + horiz_border * (width-2) + corner
    inner_row = vert_border + ' ' * (width-2) + vert_border

    for i in range(height):
        if i == 0 or i == height-1:
            print(outer_row)
        else:
            print(inner_row)


border(10,10)
border(2,8)
border(6,3)
border(2,2)
