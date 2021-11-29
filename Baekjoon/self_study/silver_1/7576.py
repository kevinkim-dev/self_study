###########################
#  BaekJoon 7576번
#  by 김승현                
###########################

# Q. 토마토

from collections import deque

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def check_all_rotten():
    for r in range(R):
        for c in range(C):
            if not tomato_box[r][c]:
                return False
    return True

def bfs(tomatos):
    max_time = 0
    while tomatos:
        r, c, time = tomatos.popleft()
        max_time = max(max_time, time)
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not tomato_box[nr][nc]:
                tomatos.append((nr, nc, time + 1))
                tomato_box[nr][nc] = time + 1
    return max_time


C, R = map(int, input().split())

tomato_box = []
tomatos = deque()

for r in range(R):
    tomato_row = list(map(int, input().split()))
    tomato_box.append(tomato_row)
    for c in range(C):
        if tomato_row[c] == 1:
            tomatos.append((r, c, 0))

ans = bfs(tomatos)

if check_all_rotten():
    print(ans)
else:
    print(-1)