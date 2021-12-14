###########################
#  BaekJoon 2887번
#  by 김승현                
###########################

# Q. 행성 터널

def find(node):
    if union_set[node] == node:
        return node
    
    union_set[node] = find(union_set[node])
    return union_set[node]

def union(a, b):
    ap = find(a)
    bp = find(b)

    if ap == bp:
        return False
    
    if ap > bp:
        union_set[ap] = bp
    else:
        union_set[bp] = ap
    return True

def kruskal():
    cost = 0
    for dist, a, b in tunnels:
        if union(a, b):
            cost += dist
    return cost

N = int(input())
MD = 2*10**9 + 1

planets = []
tunnels = []
for i in range(N):
    x, y, z = map(int, input().split())
    planets.append([x, y, z, i])

planets.sort(key=lambda x: x[0])
for i in range(N-1):
    tunnels.append((abs(planets[i][0] - planets[i+1][0]), planets[i][3], planets[i+1][3]))

planets.sort(key=lambda x: x[1])
for i in range(N-1):
    tunnels.append((abs(planets[i][1] - planets[i+1][1]), planets[i][3], planets[i+1][3]))

planets.sort(key=lambda x: x[2])
for i in range(N-1):
    tunnels.append((abs(planets[i][2] - planets[i+1][2]), planets[i][3], planets[i+1][3]))

tunnels.sort(key=lambda x: x[0])

union_set = [i for i in range(N)]

print(kruskal())




# def prim():
#     cost = 0
#     node = 0
#     visited = [0]*N
#     visited[0] = 1
#     visit_cnt = 1
#     while visit_cnt < N:
#         D = MD
#         for i in range(N):
#             if i == node or visited[i]:
#                 continue
#             if adj_list[node][i] < D:
#                 D = adj_list[node][i]
#                 next = i
#         visited[next] = 1
#         node = next
#         cost += D
#         visit_cnt += 1
#     return cost

# N = int(input())
# MD = 2*10**9 + 1
# adj_list = [[MD]*N for _ in range(N)]

# planets = []

# for i in range(N):
#     x, y, z = map(int, input().split())
#     for j in range(i):
#         nx, ny, nz = planets[j]
#         dist = min(abs(nx-x), abs(ny-y), abs(nz-z))
#         adj_list[i][j] = dist
#         adj_list[j][i] = dist
#     planets.append([x, y, z])

# print(prim())