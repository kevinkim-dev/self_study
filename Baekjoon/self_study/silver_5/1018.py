###########################
#  BaekJoon 1018번
#  by 김승현                
###########################

# Q. 체스판 다시 칠하기

black_white = ['B', 'W']
N, M = map(int, input().split())
board = list(list(input()) for _ in range(N))
new_board = list([0]*M for _ in range(N))
for i in range(N):
    for j in range(M):
        if black_white[(i + j) % 2] != board[i][j]:
            new_board[i][j] = 1
min_cnt = 64
for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for r in range(8):
            for c in range(8):
                if new_board[i + r][j + c] == 1:
                    cnt += 1
        min_cnt = min(min_cnt, cnt, 64-cnt)
print(min_cnt)

