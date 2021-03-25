#########################
#  SWEA number 10580
#  by 김승현                
#########################

# Q. 전봇대

for t in range(1, int(input())+1):
    N = int(input())
    line_list = []
    for n in range(N):
        line_list.append(list(map(int, input().split())))
    line_list = sorted(line_list, key = lambda x: x[0])
    cross = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if line_list[i][1] - line_list[j][1] > 0:
                cross += 1
    print("#%d %d" %(t, cross))