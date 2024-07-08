input_str = input()
hour, minute = input_str.split()
hour = int(hour)
minute = int(minute)

minute -= 45
if (minute < 0):
    minute = 60 + minute
    hour -= 1

if (hour == -1):
    hour = 23

print(hour, minute)