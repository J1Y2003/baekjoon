N = int(input())
divisor = 2
while (N != 1):
    if (N % divisor == 0):
        print(divisor)
        N /= divisor
        divisor = 2
    else:
        divisor += 1