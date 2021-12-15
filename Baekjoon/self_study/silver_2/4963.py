###########################
#  BaekJoon 4963번
#  by 김승현                
###########################

# Q. 섬의 개수

drc = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def bfs(row, col):
    q = [(row, col)]
    while q:
        r, c = q.pop()
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and jido[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
    return



while True:
    C, R = map(int, input().split())
    if not C and not R:
        break
    jido = []
    for _ in range(R):
        jido.append(list(map(int, input().split())))
    visited = [[0]*C for _ in range(R)]
    ans = 0
    for r in range(R):
        for c in range(C):
            if visited[r][c] or not jido[r][c]:
                continue
            bfs(r, c)
            ans += 1
    print(ans)