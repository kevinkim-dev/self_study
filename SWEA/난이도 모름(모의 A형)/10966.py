#########################
#  SWEA number 10966
#  by 김승현                
#########################

# Q. 물놀이를 가자 ( 시간 제한 초과 )

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def find_water():
    water = []
    for i in range(N):
        for j in range(M):
            if pool[i][j] == '0':
                pool[i][j] = 0
                water.append((i, j))
    return water

def find_route(l):
    for _ in range(len(q)):
        pos = q.pop(0)
        r, c = pos
        for d in dxy:
            new_r = r + d[0]
            new_c = c + d[1]
            if 0 <= new_r <= N-1 and 0 <= new_c <= M-1 and (new_r, new_c) not in visited:
                q.append((new_r, new_c))
                visited.append((new_r, new_c))
                pool[new_r][new_c] = l
    if not q:
        return
    else:
        find_route(l+1)

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    pool = [list(input().replace('W', '0')) for _ in range(N)]
    q = find_water()
    visited = q[:]
    find_route(1)
    ans = 0
    for n in range(N):
        ans += sum(pool[n])
    print("#%d %d" %(t, ans))