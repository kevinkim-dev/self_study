###########################
#  BaekJoon 5567번
#  by 김승현                
###########################

# Q. 결혼식

import sys

input = sys.stdin.readline

def dfs(root, leg):
    q = [(root, leg)]
    ans = 0
    while q:
        node, l = q.pop(0)
        ans += 1
        if l > 1:
            continue
        for i in range(N):
            if adj_matrix[node][i] and not visited[i]:
                q.append((i, l+1))
                visited[i] = 1
    return ans

N, M = int(input()), int(input())

adj_matrix = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_matrix[a-1][b-1] = 1
    adj_matrix[b-1][a-1] = 1

visited = [0]*N
visited[0] = 1

print(dfs(0, 0)-1)