###########################
#  BaekJoon 1012번
#  by 김승현                
###########################

# Q. 유기농 배추

def dfs(ro, co):
    q = [(ro, co)]
    visited[ro][co] = 1
    while q:
        r, c = q.pop(0)
        for dr, dc in dxy:
            nr, nc = r + dr, c + dc
            if 0 <= nr <= row-1 and 0 <= nc <= col-1 and ground[nr][nc] and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return


dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(int(input())):
    cnt = 0
    col, row, N = map(int, input().split())
    ground = [[0]*col for _ in range(row)]
    visited = [[0]*col for _ in range(row)]
    for _ in range(N):
        y, x = map(int, input().split())
        ground[x][y] = 1
    for r in range(row):
        for c in range(col):
            if ground[r][c] and not visited[r][c]:
                dfs(r, c)
                cnt += 1
    print(cnt)
