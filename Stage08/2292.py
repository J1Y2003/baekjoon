N = int(input())
cnt = 1
cur = 1
add = 6
while (N > cur):
    cur += add * cnt
    cnt += 1

print(cnt)