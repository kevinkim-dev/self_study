###########################
#  BaekJoon 14496번
#  by 김승현                
###########################

# Q. 그대, 그머가 되어

from collections import deque

def bfs(s):
    q = deque()
    q.append((s, 0))
    while q:
        node, change = q.popleft()
        if node == b:
            return change
        for next in adj_list[node]:
            if visited[next]:
                continue
            q.append((next, change+1))
            visited[next] = 1
    return -1
        

import sys

input = sys.stdin.readline

a, b = map(int, input().split())

N, M = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

visited = [0]*(N+1)
visited[1] = 1

print(bfs(a))