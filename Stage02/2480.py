all_toss = input()
first, second, third = [int(x) for x in all_toss.split()]
if (first == second and second == third):
    prize = 10000 + first * 1000
elif (first == second or second == third):
    prize = 1000 + second * 100
elif (first == third):
    prize = 1000 + first * 100
else:
    prize = max(first, second, third) * 100

print(prize)