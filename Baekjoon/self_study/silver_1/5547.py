###########################
#  BaekJoon 5547번
#  by 김승현                
###########################

# Q. 일루미네이션

drc = [(0, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)]

def check_outside(row, col):
    q = [(row, col)]
    while q:
        r, c = q.pop()
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if dr:
                nc -= r % 2
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and not house[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
    return

def check_inside():
    for r in range(R):
        for c in range(C):
            if not visited[r][c] and not house[r][c]:
                house[r][c] = 1
    return

def dfs(row, col):
    wall = 0
    q = [(row, col)]
    while q:
        r, c = q.pop()
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if dr:
                nc -= r % 2
            if 0 <= nr < R and 0 <= nc < C:
                # 또 집이면
                if house[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                elif not house[nr][nc]:
                    wall += 1
            else:
                wall += 1
    return wall



C, R = map(int, input().split())

house = [list(map(int, input().split())) for _ in range(R)]

visited = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if (i == 0 or i == R-1 or j == 0 or j == C-1) and not visited[i][j] and not house[i][j]:
            visited[i][j] = 1
            check_outside(i, j)

check_inside()

ans = 0
visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if not visited[i][j] and house[i][j]:
            visited[i][j] = 1
            ans += dfs(i, j)

print(ans)