###########################
#  BaekJoon 21610번
#  by 김승현                
###########################

# Q. 마법사 상어와 비바라기

import sys

input = sys.stdin.readline

drc = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

for k in range(M):
    d, s = map(int, input().split())
    if not k:
        cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
    else:
        cloud = []
        for r in range(N):
            for c in range(N):
                if board[r][c] >= 2 and not visited[r][c]:
                    board[r][c] -=2
                    cloud.append([r, c])
    visited = [[0]*N for _ in range(N)]
    new_cloud = []
    for cr, cc in cloud:
        cr = (cr + drc[d][0]*s)%N
        cc = (cc + drc[d][1]*s)%N
        board[cr][cc] += 1
        visited[cr][cc] = 1
        new_cloud.append((cr, cc))
    for r, c in new_cloud:
        for i in range(2, 10, 2):
            nr, nc = r + drc[i][0], c + drc[i][1]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc]:
                board[r][c] += 1
ans = 0
for r in range(N):
    for c in range(N):
        if board[r][c] >= 2 and not visited[r][c]:
            board[r][c] -=2

for i in range(N):
    for j in range(N):
        ans += board[i][j]

print(ans)