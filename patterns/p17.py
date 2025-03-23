n = int(input())

for row in range(n):
    line = []

    for col in range(n):
        if row == col or row == n - col - 1:
            line.append('M')
        else:
            if row == 0 or row == n-1 or col == 0 or col == n-1:
                line.append('F')
            else:
                line.append('C')

    print(' '.join(line))
