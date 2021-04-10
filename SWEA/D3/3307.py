#########################
#  SWEA number 3307
#  by 김승현                
#########################

# Q. 최장 증가 부분 수열

def find_LIS(idx, num, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    if idx == N or N - idx < max_cnt - cnt:
        return
    if num < num_list[idx]:
        find_LIS(idx+1, num_list[idx], cnt+1)
    find_LIS(idx+1, num, cnt)
    return


for t in range(1, int(input())+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    max_cnt = 0
    for i in range(N-1):
        # idx, num, cnt
        find_LIS(i+1, num_list[i], 1)
    print("#%d %d" %(t, max_cnt))