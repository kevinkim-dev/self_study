import copy
from collections import deque

drc = [[0, -1], [0, 1], [1, 0], [-1, 0]]

def DFS(level, arr):
    global result
    if level == N:
        cnt = 0
        for h in range(H):
            cnt += arr[h].count(0)
        tmp = W*H - cnt
        if tmp < result:
            result = tmp
        return
    for c in range(W):
        for r in range(H):
            check = 0
            if not arr[r][c]:
                continue
            else:
                backup = copy.deepcopy(arr)
                Q = deque()
                Q.append((r, c, arr[r][c]))
                while Q:
                    target = Q.popleft()
                    if target[2] == 1:
                        arr[target[0]][target[1]] = 0
                    else:
                        arr[target[0]][target[1]] = 0
                        for k in range(1, target[2]):
                            for dr, dc in drc:
                                nr = target[0]+dr*k
                                nc = target[1]+dc*k
                                if 0<=nr<H and 0<=nc<W and arr[nr][nc] != 0:
                                    if (nr, nc, arr[nr][nc]) not in Q:
                                        Q.append((nr, nc, arr[nr][nc]))
                after = [[0]*W for _ in range(H)]
                for j in range(W):
                    tmpl = []
                    for i in range(H):
                        if arr[i][j]:
                            tmpl.append(arr[i][j])
                    for a in range(len(tmpl)):
                        after[H-len(tmpl)+a][j] = tmpl[a]
                check = 1
            if check == 1:
                DFS(level+1, after)
                arr = backup
            break

    DFS(N, arr)

T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(H)]
    result = 987654321
    DFS(0, brick)
    print("#%d %d" % (t, result))