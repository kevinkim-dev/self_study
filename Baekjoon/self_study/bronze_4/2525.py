###########################
#  BaekJoon 2525번
#  by 김승현                
###########################

# Q. 오븐 시계

hour, minute = map(int, input().split())
time = int(input())

new_hour = hour + (time // 60)
new_minute = (minute + (time % 60)) % 60
if minute + (time % 60) >= 60:
    new_hour += 1
new_hour %= 24

print(new_hour, new_minute)