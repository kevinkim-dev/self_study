###########################
#  BaekJoon 2606번
#  by 김승현                
###########################

# Q. 바이러스

N, E = int(input()), int(input())

net = [[0]*N for _ in range(N)]

for _ in range(E):
    s, e = map(int, input().split())
    net[s-1][e-1], net[e-1][s-1] = 1, 1

visited = [0]*N
q = [0]
visited[0] = 1
while q:
    node = q.pop()
    for i in range(N):
        if net[node][i] and not visited[i]:
            q.append(i)
            visited[i] = 1

print(sum(visited)-1)
