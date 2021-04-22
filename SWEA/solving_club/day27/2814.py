#########################
#  SWEA number 2814
#  by 김승현                
#########################

# Q. 최장 경로

def dfs(s, cnt):
    global ans
    ans = max(ans, cnt)
    visited[s] = 1
    for num in adj_list[s]:
        if not visited[num]:
            dfs(num, cnt+1)
            visited[num] = 0


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)
    ans = 0
    for i in range(1, N+1):
        visited = [0] * (N + 1)
        dfs(i, 1)
    print('#%d %d' % (t, ans))