N, K = [int(x) for x in input().split()]
divisor = []

for num in range(1, N + 1):
    if (N % num == 0):
        divisor.append(num)

if (len(divisor) < K):
    print(0)
else:
    print(divisor[K - 1])