###########################
#  BaekJoon 1697번
#  by 김승현                
###########################

# Q. 숨바꼭질 

from collections import deque

def bfs(N):
    q = deque()
    q.append((N, 0))
    while q:
        node, move = q.popleft()
        if node == K:
            return move
        if node+1 < max_num and not visited[node+1] and node < K:
            q.append((node+1, move+1))
            visited[node+1] = 1
        if node-1 >= 0 and not visited[node-1]:
            q.append((node-1, move+1))
            visited[node-1] = 1
        if node*2 < max_num and not visited[node*2] and node < K:
            q.append((node*2, move+1))
            visited[node*2] = 1
    return    


N, K = map(int, input().split())
max_num = 100001
visited = [0]*max_num
visited[N] = 1

print(bfs(N))