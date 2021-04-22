#########################
#  SWEA number 2819
#  by 김승현                
#########################

# Q. 격자판의 숫자 이어 붙이기

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def search(rc, s, l):
    if l == 7:
        nums.add(s)
        return
    r, c = rc
    for d in dxy:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr <= N-1 and 0 <= nc <= N-1:
            search((nr, nc), s + board[nr][nc], l+1)
    return

for t in range(1, int(input())+1):
    N = 4
    board = [list(input().split()) for _ in range(N)]
    nums = set()
    for i in range(N):
        for j in range(N):
            search((i, j), board[i][j], 1)
    print("#%d %d" %(t, len(nums)))