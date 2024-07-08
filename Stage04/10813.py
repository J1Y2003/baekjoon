N, M = [int(x) for x in input().split()]
baskets = list(range(1, N + 1))
for _ in range(M):
    i, j = [int(x) for x in input().split()]
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

print(*baskets)