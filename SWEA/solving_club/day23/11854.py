#########################
#  SWEA number 11854
#  by 김승현                
#########################

# Q. 화물 도크

for t in range(1, int(input())+1):
    N = int(input())
    apply = [list(map(int, input().split())) for _ in range(N)]
    max_truck = [0]*25
    for i in range(1, 25):
        max_truck[i] = max([max_truck[j] + int(bool([j, i] in apply)) for j in range(i)])
    print("#%d %d" %(t, max_truck[-1]))