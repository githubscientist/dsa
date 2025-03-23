n = int(input())

odd = 1
# row = 1 to n
for row in range(1, n+1):
    # for each line
    line = []

    for spaces in range(n-row):
        line.append(' ')

    # check if the row is first or last
    if row == 1 or row == n:
        # push row number of stars into the line
        for stars in range(row):
            line.append('*')
            line.append(' ')
    else:
        # for all the lines except first row and last row
        line.append('*')

        for spaces in range(odd):
            line.append(' ')

        odd += 2

        line.append('*')
    print(''.join(line))
