rows, cols = map(int, input().split(' '))

for row in range(1, rows+1):
    line = []

    # push cols number of stars for row=1, row = rows-1
    if (row == 1 or row == rows):
        for stars in range(cols):
            line.append('*')
    else:
        # for all other rows
        # other than 1 and rows
        for col in range(1, cols+1):
            if (col == 1 or col == cols):
                line.append('*')
            else:
                line.append(' ')

    print(' '.join(line))
