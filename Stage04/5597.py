student_list = [0] * 30
for i in range(28):
    num = int(input())
    student_list[num - 1] = 1

for idx, i in enumerate(student_list):
    if (i == 0):
        print(idx + 1)