###########################
#  BaekJoon 2530번
#  by 김승현                
###########################

# Q. 인공지능 시계

hour, minute, second = map(int, input().split())
time = int(input())

new_second = second + time % 60
time //= 60
new_minute = minute + time % 60
time //= 60
new_hour = hour + time % 24

if new_second >= 60:
    new_minute += 1
    new_second -= 60


if new_minute >= 60:
    new_hour += 1
    new_minute -= 60

if new_hour >= 24:
    new_hour -= 24

print(new_hour, new_minute, new_second)