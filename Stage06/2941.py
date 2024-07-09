croatian_words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
input_str = input()
total = 0
flag = 0

for idx, letter in enumerate(input_str):
    if (flag == 1):
        flag = 0
        continue
    elif (flag == 2):
        flag = 1
        continue
    if (input_str[idx : idx + 2] in croatian_words):
        total += 1
        flag = 1
    elif (input_str[idx : idx + 3] in croatian_words):
        total += 1
        flag = 2
    else:
        total += 1


print(total)