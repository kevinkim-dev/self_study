#########################
#  SWEA number 16235
#  by 김승현                
#########################

# Q. 나무 재테크


from collections import deque

drc = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


# input 받기
N, M, K = map(int, input().split())
charge = [list(map(int, input().split())) for _ in range(N)]
energy = [[5]*N for _ in range(N)]
ground = [[list() for _ in range(N)] for _ in range(N)]


# 초기 나무 심기
for _ in range(M):
    x, y, z = map(int, input().split())
    ground[x-1][y-1].append(z)


# K년간 진행
for _ in range(K):
    for r in range(N):
        for c in range(N):
            grown_tree = deque()
            tmp = 0
            while ground[r][c]:
                tree = ground[r][c].pop()
                if tree <= energy[r][c]:
                    energy[r][c] -= tree
                    grown_tree.appendleft(tree + 1)
                else:
                    tmp += tree // 2
            energy[r][c] += tmp
            ground[r][c] = grown_tree
    for r in range(N):
        for c in range(N):
            for tree in ground[r][c]:
                if tree % 5 == 0:
                    for dr, dc in drc:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr <= N-1 and 0 <= nc <= N-1:
                            ground[nr][nc].append(1)
    for r in range(N):
        for c in range(N):
            energy[r][c] += charge[r][c]


# 나무수 덧셈
ans = 0
for r in range(N):
    for c in range(N):
        ans += len(ground[r][c])


# 출력
print(ans)