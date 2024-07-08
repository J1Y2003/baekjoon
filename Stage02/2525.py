start_time = input()
cook_time = input()
hour, minute = start_time.split()
hour = int(hour)
minute = int(minute)
cook_time = int(cook_time)

minute += cook_time

while (minute >= 60):
    minute -= 60
    hour += 1

if (hour > 23):
    hour -= 24

print(hour, minute)