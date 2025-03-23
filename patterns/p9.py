n = int(input())

odd = 1

for row in range(1, n+1):
    line = []

    # insert n-row number of spaces
    for spaces in range(n-row):
        line.append(' ')

    # push the numbers from row to odd(inclusive) (++)
    for number in range(row, odd+1):
        line.append(str(number))

    # push the numbers from odd-1 to row (--)
    for number in range(odd-1, row-1, -1):
        line.append(str(number))

    print(''.join(line))
    odd += 2
