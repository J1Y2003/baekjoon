matrix = 9 * [9 * [0]]
max = -1
max_idx = [0, 0]
for row in range(9):
    matrix[row] = [int(x) for x in input().split()]
    for column in range(9):
        if matrix[row][column] > max:
            max = matrix[row][column]
            max_idx[0], max_idx[1] = row + 1, column + 1

print(max)
print(*max_idx)