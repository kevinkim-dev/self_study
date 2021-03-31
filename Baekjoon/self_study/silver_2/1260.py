###########################
#  BaekJoon 1260번
#  by 김승현                
###########################

# Q. DFS와 BFS

def dfs(start):
    q = [start]
    visited = []
    while q:
        go = q.pop()
        if go in visited:
            continue
        visited.append(go)
        for dest in ver_list[go]:
            if dest not in visited:
                q.append(dest)
    return visited


def bfs(start):
    q = [start]
    visited = []
    while q:
        go = q.pop(0)
        visited.append(go)
        for dest in ver_list[go]:
            if dest not in visited and dest not in q:
                q.append(dest)
    return visited


N, M, V = map(int, input().split())
ver_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    ver_list[a].append(b)
    ver_list[b].append(a)
for n in range(1, N+1):
    ver_list[n].sort(reverse=True)
print(*dfs(V))
for n in range(1, N+1):
    ver_list[n].sort()
print(*bfs(V))
