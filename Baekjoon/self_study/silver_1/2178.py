###########################
#  BaekJoon 2178번
#  by 김승현                
###########################

# Q. 미로 탐색

def search():
    pos = q[0]
    distance = 0
    while True:
        distance += 1
        way = len(q)
        for _ in range(way):
            pos = q.pop(0)
            for d in dxy:
                n_r, n_c = pos[0] + d[0], pos[1] + d[1]
                if n_r == N-1 and n_c == M-1:
                    return distance + 1
                if 0 <= n_r <= N-1 and 0 <= n_c <= M-1 and maze[n_r][n_c] == '1':
                    maze[n_r][n_c] = distance
                    q.append((n_r, n_c))


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
maze = [list(input()) for n in range(N)]
q = [(0, 0)]
print(search())

2, 3   -1, 0

