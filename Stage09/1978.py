_ = int(input())
test_cases = [int(x) for x in input().split()]
cnt = 0
for num in test_cases:
    if (num == 1):
         continue
    flag = 0
    for divide in range(2, num):
            if (num % divide == 0):
                flag = 1
                break
    if (flag == 0):
         cnt += 1

print(cnt)