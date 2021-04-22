#########################
#  SWEA number 2806
#  by 김승현                
#########################

# Q. N-Queen

def NQueen(r):
    global cnt
    if r == N:
        cnt += 1
        return
    for col in range(N):
        if cols[col] or cross1[r + col] or cross2[N + r - col - 1]:
            continue
        cols[col] = cross1[r + col] = cross2[N + r - col - 1] = 1
        NQueen(r+1)
        cols[col] = cross1[r + col] = cross2[N + r - col - 1] = 0
 
 
for t in range(1, int(input())+1):
    N = int(input())
    cols = [0] * N
    cross1, cross2 = [0] * (N*2-1), [0] * (N*2-1)
    cnt = 0
    NQueen(0)
    print("#%d %d" % (t, cnt))