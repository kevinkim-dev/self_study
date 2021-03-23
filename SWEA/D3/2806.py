#########################
#  SWEA number 2806
#  by 김승현                
#########################

# Q. N-Queen

dxy = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))


def queen(q_num):
    global ans
    if q_num == N:
        ans += 1
        return
    for n in range(N):
        if board[q_num][n] == -1:
            board[q_num][n] = 'q'
            board_set(q_num, n)
            queen(q_num + 1)
            board[q_num][n] = -1
            board_erase(q_num, n)
    return

def board_set(q_num, n):
    loc_r, loc_c = q_num, n
    for d in dxy:
        for length in range(1, N):
            d_r, d_c = loc_r + d[0]*length, loc_c + d[1]*length
            if not 0 <= d_r <= N-1 or not 0 <= d_c <= N-1:
                break
            elif board[d_r][d_c] == -1:
                board[d_r][d_c] = q_num
    return


def board_erase(q_num, n):
    loc_r, loc_c = q_num, n
    for d in dxy:
        for length in range(1, N):
            d_r, d_c = loc_r + d[0]*length, loc_c + d[1]*length
            if not 0 <= d_r <= N-1 or not 0 <= d_c <= N-1:
                break
            elif board[d_r][d_c] == q_num:
                board[d_r][d_c] = -1
    return



for t in range(1, int(input())+1):
    N = int(input())
    board = [[-1]*N for _ in range(N)]
    ans = 0
    queen(0)
    print("#%d %d" %(t, ans))
