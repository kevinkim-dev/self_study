#########################
#  SWEA number 11625
#  by 김승현                
#########################

# Q. BFS 코드 작성

def BFS(x):
    cnt = 0
    for n in to_go[x]:
        if n not in visited and n not in q:
            q.append(n)
            cnt += 1
    for _ in range(cnt):
        visited.append(q[0])
        BFS(q.pop(0))

t = int(input())
N, V = map(int, input().split())
to_go = [[] for _ in range(N+1)]
for i in range(V):
    s, e = map(int, input().split())
    to_go[s].append(e)
q = [1]
visited = [1]
BFS(q.pop(0))
print("#%d" %t, end=' ')
print(*visited)
