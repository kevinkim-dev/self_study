###########################
#  BaekJoon 5575번
#  by 김승현                
###########################

# Q. 타임 카드

time_list = [list(map(int, input().split())) for _ in range(3)]

for time in time_list:
    second = time[5] - time[2]
    minute = time[4] - time[1]
    hour = time[3] - time[0]
    if second < 0:
        second += 60
        minute -= 1
    if minute < 0:
        minute += 60
        hour -= 1
    print(hour, minute, second)