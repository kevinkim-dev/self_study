#########################
#  SWEA number 1753
#  by 김승현                
#########################

# Q. 최단경로

from collections import deque



def dijkstra(root):
    D[root] = 0
    visited = [0]*(V+1)
    while True:
        node = 0
        min_cost = 987654321
        for i in range(1, V+1):
            if visited[i]:
                continue
            if D[i] < min_cost:
                min_cost = D[i]
                node = i
        if not node:
            break
        visited[node] = 1
        if not graph.get(node):
            continue
        for next in graph[node].keys():
            D[next] = min(graph[node][next]+D[node], D[next]) 
    return

V, E = map(int, input().split())
root = int(input())

graph = dict()

INF = float('inf')
D = [INF]*(V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    if not graph.get(u):
        graph[u] = dict()
        graph[u][v] = w
    elif not graph[u].get(v):
        graph[u][v] = w
    else:
        graph[u][v] = min(graph[u][v], w)

dijkstra(root)

for i in range(1, len(D)):
    if D[i] == INF:
        print('INF')
    else:
        print(D[i])

# def dijkstra(root):
#     D[root] = 0
#     visited = [0]*(V+1)
#     q = deque()
#     q.append(root)
#     visited[root] = 1
#     while q:
#         node = q.popleft()
#         if not graph.get(node):
#             continue
#         for next in graph[node].keys():
#             if visited[next]:
#                 continue
#             D[next] = min(graph[node][next]+D[node], D[next]) 
#             q.append(next)
#             visited[next] = 1
#     return

# def dijkstra(root):
#     D[root] = 0
#     visited = [0]*(V+1)
#     q = deque()
#     q.append(root)
#     visited[root] = 1
#     while q:
#         node = q.popleft()
#         if not graph.get(node):
#             continue
#         for next in graph[node]:
#             if visited[next]:
#                 continue
#             D[next] = min(graph_weight[node][next]+D[node], D[next]) 
#             q.append(next)
#             visited[next] = 1
#     return

# V, E = map(int, input().split())
# root = int(input())

# graph = dict()
# graph_weight = [[11]*(V+1) for _ in range(V+1)]

# INF = float('inf')
# D = [INF]*(V+1)

# for _ in range(E):
#     u, v, w = map(int, input().split())
#     if not graph.get(u):
#         graph[u] = {v}
#     else:
#         graph[u].add(v)
#     graph_weight[u][v] = min(graph_weight[u][v], w)

# dijkstra(root)

# for i in range(1, len(D)):
#     if D[i] == INF:
#         print('INF')
#     else:
#         print(D[i])
