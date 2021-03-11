#########################
#  SWEA number 1953
#  by 김승현                
#########################

# Q. 탈주범 검거

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ways = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [1, 2], [2, 3], [0, 3]]

def runaway(runtime):
    if runtime >= time:
        return
    for _ in range(len(q)):
        pos = q.pop(0)
        r = pos[0]
        c = pos[1]
        for way in ways[tunnel[r][c]]:
            new_r = r + dxy[way][0]
            new_c = c + dxy[way][1]
            if 0 <= new_r <= N-1 and 0 <= new_c <= M-1 and (way+2) % 4 in ways[tunnel[new_r][new_c]] and (new_r, new_c) not in visited:
                q.append((new_r, new_c))
                visited.append((new_r, new_c))
    runtime += 1
    runaway(runtime)

for t in range(1, int(input())+1):
    N, M, x, y, time = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    q = [(x, y)]
    visited = [(x, y)]
    runaway(1)
    print("#%d %d" %(t, len(visited)))