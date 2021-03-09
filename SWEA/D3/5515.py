#########################
#  SWEA number 5515
#  by 김승현                
#########################

# Q. 2016년 요일 맞추기

day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, int(input())+1):
    month, day = map(int, input().split())
    dif = (day - 1 + sum(day_list[:month-1]) +4) % 7
    print("#%d %d" %(t, dif))
    
    # for i in range(1, month):
    #     dif += day_list[]