N, M = [int(x) for x in input().split()]

matrix = [[0] * M] * N
for row in range(N):
    matrix[row] = [int(x) for x in input().split()]

for row in range(N):
    add_column = [int(x) for x in input().split()]
    for column in range(M):
        matrix[row][column] += add_column[column]

for row in matrix:
    print(*row)