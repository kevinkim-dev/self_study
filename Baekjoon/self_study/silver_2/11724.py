###########################
#  BaekJoon 11724번
#  by 김승현                
###########################

# Q. 연결 요소의 개수

def dfs(root):
    q = [root]
    while q:
        node = q.pop()
        for next in adj_list[node]:
            if visited[next]:
                continue
            visited[next] = 1
            q.append(next)
    return

N, M = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

visited = [0]*(N+1)
ans = 0

for i in range(1, N+1):
    if visited[i]:
        continue
    visited[i] = 1
    ans += 1
    dfs(i)

print(ans)