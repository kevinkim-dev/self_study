#########################
#  SWEA number 2206
#  by 김승현                
#########################

# Q. 벽 부수고 이동하기

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

R, C = map(int, input().split())

ans = -1

game_map = [list(map(int, list(input()))) for _ in range(R)]

visited = [[[0, 0] for _ in range(C)] for _ in range(R)]
visited[0][0][0] = 1

q = [(0, 0, 0)]
while q:
    r, c, boom = q.pop(0)
    if r == R-1 and c == C-1:
        ans = visited[r][c][boom]
        break
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if game_map[nr][nc] and not boom and not visited[nr][nc][boom]:
                visited[nr][nc][1] = visited[r][c][0] + 1
                q.append((nr, nc, 1))
            elif not game_map[nr][nc] and not visited[nr][nc][boom]:
                visited[nr][nc][boom] = visited[r][c][boom] + 1
                q.append((nr, nc, boom))

print(ans)