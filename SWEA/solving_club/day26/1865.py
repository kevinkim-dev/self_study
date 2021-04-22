#########################
#  SWEA number 1865
#  by 김승현                
#########################

# Q. 동철이의 일 분배

import sys

import sys
sys.stdin = open("input.txt", "r")

def work(row, pro):
    global max_pro
    if row == N:
        if pro > max_pro:
            max_pro = pro
        return
    if not pro or pro*max_row[row] <= max_pro:
        return
    for col in range(N):
        if cols[col]:
            continue
        cols[col] = 1
        work(row + 1, pro*pro_map[row][col])
        cols[col] = 0
    return


for t in range(1, int(input())+1):
    N = int(input())
    pro_map = [list(map(int, input().split())) for _ in range(N)]
    max_row = [max(pro_map[i]) for i in range(N)]
    for i in range(N-2, -1, -1):
        max_row[i] = max_row[i+1]*max_row[i]
    cols = [0]*N
    max_pro = 0
    work(0, 1)
    print("#%d %f" %(t, max_pro * 0.01 ** (N-1)))