GPA = []
grades = {"A+" : 4.5,
          "A0" : 4.0,
          "B+" : 3.5,
          "B0" : 3.0,
          "C+" : 2.5,
          "C0" : 2.0,
          "D+" : 1.5,
          "D0" : 1.0,
          "F" : 0.0,}

total_grade = 0
total_worth = 0
PF_count = 0
for _ in range(20):
    _, worth, grade = input().split()
    if (grade == "P"):
        PF_count += 1
        continue
    total_grade += float(worth) * grades[grade]
    total_worth += float(worth)

GPA_average = total_grade / total_worth
print(GPA_average)