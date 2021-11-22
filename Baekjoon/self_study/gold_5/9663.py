#########################
#  SWEA number 9663
#  by 김승현                
#########################

# Q. N-Queen


def nQueen(r, cols, ls, rs):
    global ans
    if r == N:
        ans += 1
        return
    for c in range(N):
        if c not in cols and r+c not in ls and r-c not in rs:
            nQueen(r+1, cols + [c], ls + [r+c], rs + [r-c])
    return

N = int(input())

ans = 0

nQueen(0, [], [], [])

print(ans)
