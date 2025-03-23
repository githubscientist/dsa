tc = int(input())

while tc > 0:
    N = int(input())

    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split(' '))))

    inversions = 0

    # traverse the matrix
    for i in range(N):
        for j in range(N):
            for p in range(i, N):
                for q in range(j, N):
                    if matrix[i][j] > matrix[p][q]:
                        inversions += 1

    print(inversions)

    tc -= 1
