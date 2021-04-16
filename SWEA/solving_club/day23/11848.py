#########################
#  SWEA number 11848
#  by 김승현                
#########################

# Q. 전자카트

def admin(area, battery, v):
    global min_battery
    if len(v) == N:
        min_battery = min(min_battery, battery + energy[area][1])
        return
    for i in range(2, N+1):
        if i not in v:
            admin(i, battery + energy[area][i], v + [i])
    return

for t in range(1, int(input())+1):
    N = int(input())
    energy = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for n in range(N)]
    visited = [1]
    min_battery = float('inf')
    admin(1, 0, visited)
    print("#%d %d" %(t, min_battery))