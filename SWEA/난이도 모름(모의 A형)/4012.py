#########################
#  SWEA number 4012
#  by 김승현                
#########################

# Q. 요리사

def cook(a, b):
    global min_dif
    a_mat = 0
    b_mat = 0
    for i in range(1, N//2):
        for j in range(i):
            a_mat += synergy[a[j]][a[i]-a[j]-1]
            b_mat += synergy[b[j]][b[i]-b[j]-1]
    min_dif = min(min_dif, abs(a_mat-b_mat))

def divide(a, b, num):
    if num == N:
        cook(a, b)
    else:
        if len(a) < N//2:
            divide(a + [num], b, num+1)
        if len(b) < N//2:
            divide(a, b + [num], num+1)
    return
    

for t in range(1, int(input())+1):
    N = int(input())
    syn = [list(map(int, input().split())) for _ in range(N)]
    synergy = [[] for _ in range(N-1)]
    for i in range(1, N):
        for j in range(i):
            synergy[j].append(syn[i][j] + syn[j][i])
    min_dif = float('inf')
    divide([0], [], 1)
    print("#%d %d" %(t, min_dif))