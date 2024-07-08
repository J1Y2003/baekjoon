N, M = [int(x) for x in input().split()]

baskets = [0] * N

for _ in range(M):
    start, end, num = [int(x) for x in input().split()]
    for idx in range(start - 1, end):
        baskets[idx] = num

print(*baskets)