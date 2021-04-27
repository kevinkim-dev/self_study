#########################
#  SWEA number 1249
#  by 김승현                
#########################

# Q. 보급로

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dijkstra(row, col):
    q = [(row, col, 0)]
    while q:
        r, c, cost  = q.pop(0)
        if nodes[r][c] >= cost:
            for d in dxy:
                n_r, n_c = r + d[0], c + d[1]
                if 0 <= n_r <= N-1 and 0 <= n_c <= N-1:
                    co = cost_map[n_r][n_c]
                    if co + cost < nodes[n_r][n_c]:
                        nodes[n_r][n_c] = co + cost
                        q.append((n_r, n_c, co + cost))
    return nodes[N-1][N-1]


for t in range(1, int(input())+1):
    N = int(input())
    cost_map = [list(map(int, list(input()))) for _ in range(N)]
    nodes = [[float('inf')]*N for _ in range(N)]
    nodes[0][0] = 0
    ans = dijkstra(0, 0)
    print("#%d %d" %(t, ans))
