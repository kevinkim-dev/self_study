#########################
#  SWEA number 4615
#  by 김승현                
#########################

# Q. 재미있는 오셀로 게임

def row_check(row, col, player, playbox):
    # 왼쪽 check
    i = 1
    while i <= col:
        if playbox[row][col-i] == player:
            for idx in range(1, i):
                playbox[row][col-idx] = player
            break
        elif playbox[row][col-i] == 0:
            break
        else:
            i += 1
    # 오른쪽 check
    i = 1
    while i <= N - col -1:
        if playbox[row][col+i] == player:
            for idx in range(1, i):
                playbox[row][col+idx] = player
            break
        elif playbox[row][col+i] == 0:
            break
        else:
            i += 1
    return

def col_check(row, col, player, playbox):
    # 위쪽 check
    i = 1
    while i <= row:
        if playbox[row-i][col] == player:
            for idx in range(1, i):
                playbox[row-idx][col] = player
            break
        elif playbox[row-i][col] == 0:
            break
        else:
            i += 1
    # 아래쪽 check
    i = 1
    while i <= N - row - 1:
        if playbox[row+i][col] == player:
            for idx in range(1, i):
                playbox[row+idx][col] = player
            break
        elif playbox[row+i][col] == 0:
            break
        else:
            i += 1
    return

def cross_check(row, col, player, playbox):
    # 오른쪽 아래 check
    i = 1
    while i <= min(N - row -1, N - col -1):
        if playbox[row+i][col+i] == player:
            for idx in range(1, i):
                playbox[row+idx][col+idx] = player
            break
        elif playbox[row+i][col+i] == 0:
            break
        else:
            i += 1
    # 왼쪽 위 check
    i = 1
    while i <= min(row, col):
        if playbox[row-i][col-i] == player:
            for idx in range(1, i):
                playbox[row-idx][col-idx] = player
            break
        elif playbox[row-i][col-i] == 0:
            break
        else:
            i += 1
    # 오른쪽 위 check
    i = 1
    while i <= min(row, N - col -1):
        if playbox[row-i][col+i] == player:
            for idx in range(1, i):
                playbox[row-idx][col+idx] = player
            break
        elif playbox[row-i][col+i] == 0:
            break
        else:
            i += 1
    # 왼쪽 아래 check
    i = 1
    while i <= min(N - row -1, col):
        if playbox[row+i][col-i] == player:
            for idx in range(1, i):
                playbox[row+idx][col-idx] = player
            break
        elif playbox[row+i][col-i] == 0:
            break
        else:
            i += 1
    return

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    playbox = [[0]*N for n in range(N)]
    playbox[N//2-1][N//2-1] = 2
    playbox[N//2][N//2] = 2
    playbox[N//2-1][N//2] = 1
    playbox[N//2][N//2-1] = 1

    for m in range(M):
        row, col, player = map(int, input().split())
        row -= 1
        col -= 1
        playbox[row][col] = player
        row_check(row, col, player, playbox)
        col_check(row, col, player, playbox)
        cross_check(row, col, player, playbox)
    player1_cnt = 0
    player2_cnt = 0
    for i in range(N):
        for j in range(N):
            if playbox[i][j] == 1:
                player1_cnt += 1
            elif playbox[i][j] == 2:
                player2_cnt += 1
    print("#%d %d %d" %(t, player1_cnt, player2_cnt))