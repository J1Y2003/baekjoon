year = int(input())
leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print(int(leap))