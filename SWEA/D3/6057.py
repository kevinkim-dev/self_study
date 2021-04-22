#########################
#  SWEA number 6057
#  by 김승현                
#########################

# Q. 그래프의 삼각형

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    adj_list = [list() for _ in range(N+1)]
    for _ in range(M):
        x, y = sorted(list(map(int, input().split())))
        adj_list[x].append(y)
    cnt = 0
    for i in range(N):
        for j in adj_list[i]:
            for k in adj_list[j]:
                if k in adj_list[i]:
                    cnt += 1
    print("#%d %d" %(t, cnt))
