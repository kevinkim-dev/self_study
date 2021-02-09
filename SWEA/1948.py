#########################
#  SWEA number 1948
#  by 김승현                
#########################

# Q. 날짜 계산기

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for t in range(1, T+1):
    _sum = 1
    first_month, first_day, second_month, second_day = map(int, input().split())
    for i in range(first_month, second_month+1):
        _sum += day[i]
    _sum -= first_day
    _sum -= day[second_month] - second_day
    print("#%d %d" % (t, _sum))