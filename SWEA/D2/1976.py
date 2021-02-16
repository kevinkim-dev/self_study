#########################
#  SWEA number 1976
#  by 김승현 
#########################

# Q. 시각 덧셈

for t in range(1, int(input())+1):
    h1, m1, h2, m2 = map(int, input().split())
    hour = h1+h2
    minute = m1+m2
    if minute > 59:
        hour += 1
        minute -= 60
    if hour > 12:
        hour -= 12
    print("#%d %d %d" %(t, hour, minute))