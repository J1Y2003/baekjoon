total = int(input())
purchased_num = int(input())
real_total = 0

for _ in range(purchased_num):
    price, num = [int(x) for x in input().split()]
    real_total += price * num

if (total == real_total):
    print("Yes")
else:
    print("No")