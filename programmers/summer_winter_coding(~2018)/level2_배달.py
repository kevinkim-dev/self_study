def solution(N, road, K):
    def dijkstra(limit):
        q = []
        for i in range(2, N+1):
            if graph[1][i]:
                D[i] = graph[1][i]
                q.append(i)
        while q:
            now = q.pop(0)
            if D[now] >= limit:
                continue
            for i in range(2, N+1):
                if graph[now][i] and D[now] + graph[now][i] < D[i]:
                    D[i] = D[now] + graph[now][i]
                    q.append(i)
        return
            
            
    answer = 0
    D = [float('inf')]*(N+1)
    D[1] = 0
    graph = [[0]*(N+1) for _ in range(N+1)]
    for a, b, c in road:
        if graph[a][b] and graph[a][b] < c: 
            continue
        graph[a][b], graph[b][a] = c, c
    dijkstra(K)
    for i in range(1, N+1):
        if D[i] <= K:
            answer += 1
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

print(solution(N, road, K))