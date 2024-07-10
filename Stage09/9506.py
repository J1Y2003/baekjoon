while (True):
    N = int(input())
    if (N == -1):
        break

    divisor = []
    for num in range(1, N):
        if (N % num == 0):
            divisor.append(num)
    if (sum(divisor) == N):
        print(N, "= ", end="")
        print(*divisor, sep=" + ")
    else:
        print(N, "is NOT perfect.")