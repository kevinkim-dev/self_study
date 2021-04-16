#########################
#  SWEA number 11847
#  by 김승현                
#########################

# Q. 최소합


for t in range(1, int(input())+1):
    N = int(input())
    board = [[0] +list(map(int, input().split())) for _ in range(N)]
    board = [[0]*(N+1)] + board

    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j-1] and board[i-1][j]:
                board[i][j] += min(board[i][j-1], board[i-1][j])
            else:
                board[i][j] += board[i][j-1] + board[i-1][j]
    print("#%d %d" %(t, board[N][N]))