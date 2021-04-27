#########################
#  SWEA number 11908
#  by 김승현                
#########################

# Q. powerset 만들기

def power_set(idx, s):
    global cnt
    if s >= M or idx == N:
        if s == M:
            cnt += 1
        return
    power_set(idx+1, s + num_list[idx])
    power_set(idx+1, s)

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    cnt = 0
    power_set(0, 0)
    print("#%d %d" %(t, cnt))