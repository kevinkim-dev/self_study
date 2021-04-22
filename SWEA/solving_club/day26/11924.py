#########################
#  SWEA number 11924
#  by 김승현                
#########################

# Q. 최소생산비용


def factory(row, cost):
    global min_cost
    if cost >= min_cost:
        return
    if row == N:
        min_cost = min(min_cost, cost)
        return
    for col in range(N):
        if cols[col]:
            continue
        cols[col] = 1
        factory(row + 1, cost + table[row][col])
        cols[col] = 0
    return
 
 
for t in range(1, int(input())+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cols = [0]*N
    min_cost = float('inf')
    factory(0, 0)
    print("#%d %d" % (t, min_cost))