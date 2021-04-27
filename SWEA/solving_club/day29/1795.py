#########################
#  SWEA number 1795
#  by 김승현                
#########################

# Q. 인수의 생일 파티

def dijkstra(x, graph):
    costs = [float('inf')]*(N+1)
    U = set()
    U.add(x)
    for node, weight in graph[x]:
        costs[node] = weight
    while U != set(range(1, N+1)):
        min_w = float('inf')
        min_i = -1
        for i in range(1, N+1):
            if i in U:
                continue
            if costs[i] < min_w:
                min_w = costs[i]
                min_i = i
        w = min_i
        U.add(w)
        for no, we in graph[w]:
            costs[no] = min(costs[no], costs[w] + we)
    return costs

for t in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]
    r_adj_list = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        adj_list[s].append((e, w))
        r_adj_list[e].append((s, w))
    go_cost = dijkstra(X, adj_list)
    back_cost = dijkstra(X, r_adj_list)
    max_cost = 0
    for i in range(1, N+1):
        if i == X:
            continue
        max_cost = max(max_cost, go_cost[i] + back_cost[i])
    print("#%d %d" %(t, max_cost))
    