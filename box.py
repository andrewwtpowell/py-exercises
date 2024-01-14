def drawBox(size):

    if size < 1:
        return None

    h_line = '-'
    v_line = '|'
    d_line = '/'
    corner = '+'

    h_edge = corner + h_line*size*2 + corner
    first_line = ' '*(size+1) + h_edge
    mid_line = h_edge + ' '*size + corner
    last_line = h_edge

    print(first_line)
    for i in range(size):
        line = ' '*(size-i) + d_line + ' '*i + v_line + ' '*(size*2-(i+1)) + d_line + ' '*i + v_line
        print(line)
    print(mid_line)
    for i in range(size):
        line = v_line + ' '*(size-1-i) + d_line + ' '*(size+i) + v_line + ' '*(size-1-i) + d_line
        print(line)
    print(last_line)


for i in range(7):
    drawBox(i)
