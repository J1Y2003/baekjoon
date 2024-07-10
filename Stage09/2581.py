M = int(input())
N = int(input())
prime = []
for num in range(M, N + 1):
    if (num == 1):
         continue
    flag = 0
    for divide in range(2, num):
            if (num % divide == 0):
                flag = 1
                break
    if (flag == 0):
         prime.append(num)
if (len(prime) == 0):
     print(-1)
else:
    print(sum(prime))
    print(min(prime))