#########################
#  SWEA number 1226
#  by 김승현                
#########################

# Q. 미로1

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def BFS():
    while q:
        info = q.pop(0)
        miro[info[0]][info[1]] = 1
        for d in dxy:
            r, c = info[0] + d[0], info[1] + d[1]
            if (not 0 <= r <= N-1) or (not 0 <= c <= N-1) or miro[r][c] == 1:
                continue
            elif miro[r][c] == 3:
                return 1
            else:
                q.append((r, c))      
    return 0

def start():
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                return i, j

for _ in range(1, 11):
    t = int(input())
    N = 16
    miro = [list(map(int, input())) for _ in range(N)]
    q = [start()]
    visited = [start()]
    print("#%d %d" %(t, BFS()))