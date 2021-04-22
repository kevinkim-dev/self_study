#########################
#  SWEA number 1861
#  by 김승현                
#########################

# Q. 정사각형 방

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(loc):
    r, c = loc[0], loc[1]
    for d in dxy:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr <= N-1 and 0 <= nc <= N-1 and rooms[r][c] + 1 == rooms[nr][nc]:
            if rooms_dp[nr][nc] == 0:
                rooms_dp[r][c] = dfs((nr, nc)) + 1
                return rooms_dp[r][c]
            else:
                rooms_dp[r][c] = rooms_dp[nr][nc] + 1
                return rooms_dp[r][c]
    rooms_dp[r][c] = 1
    return 1


for t in range(1, int(input())+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    rooms_dp = [[0]*N for _ in range(N)]
    max_move = 0
    max_move_room = N**2+1
    for i in range(N):
        for j in range(N):
            if rooms_dp[i][j] == 0:
                dfs((i, j))
            if rooms_dp[i][j] > max_move:
                max_move = rooms_dp[i][j]
                max_move_room = rooms[i][j]
            elif rooms_dp[i][j] == max_move:
                max_move_room = min(max_move_room, rooms[i][j])
    # print(rooms_dp)
    print("#%d %d %d" %(t, max_move_room, max_move))
