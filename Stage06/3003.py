cur_amount = [int(x) for x in input().split()]
correct_amount = [1, 1, 2, 2, 2, 8]
print(*[correct - cur for correct, cur in zip(correct_amount, cur_amount)])