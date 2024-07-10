X = int(input())
step = 1
num, den = 0, 0
while (X > step):
    X -= step
    step += 1
even = (step % 2 == 0)

if even:
    den = step
    num = 1
else:
    den = 1
    num = step

for _ in range(X - 1):
    if even:
        den -= 1
        num += 1
    else:
        den += 1
        num -= 1

print(num, "/", den, sep="")



""" timeout solution:
limit = 1
num = 1
den = 1
flag = 1 #flag = 0 indicates numerator increase, = 1 indicates denominator increase
for _ in range(int(input()) - 1):
    if (flag == 0):
        if (num == limit):
            limit += 1
            flag = 1
            num += 1
        else:
            num += 1
            den -= 1
    else:
        if (den == limit):
            limit += 1
            flag = 0
            den += 1
        else:
            num -= 1
            den += 1
        
print(num, "/", den, sep="")
"""