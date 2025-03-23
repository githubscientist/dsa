n = int(input())

for row in range(1, n+1):
    # for every row
    # print n-row+1 number of stars
    line = []

    for star in range(0, n-row+1):
        line.append('*')

    print('  '.join(line))
