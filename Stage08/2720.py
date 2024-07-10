for _ in range(int(input())):
    total = int(input())
    changes = [0, 0, 0, 0]
    changes[0] = int(total/25)
    total %= 25
    changes[1] = int(total/10)
    total %= 10
    changes[2] = int(total/5)
    total %= 5
    changes[3] = int(total/1)
    total %= 1
    print(*changes)