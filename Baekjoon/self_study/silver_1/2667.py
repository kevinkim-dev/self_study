###########################
#  BaekJoon 2667번
#  by 김승현                
###########################

# Q. 단지번호붙이기

drc = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def dfs(i, j):
    q = [(i, j)]
    house_list.append(0)
    while q:
        r, c = q.pop()
        house_list[-1] += 1
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0<= nr < N and 0 <= nc < N and not visited[nr][nc] and house_map[nr][nc] == '1':
                q.append((nr, nc))
                visited[nr][nc] = 1
    return

N = int(input())

house_map = []

for _ in range(N):
    house_map.append(input())

house_list = []
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        if house_map[i][j] == '1':
            visited[i][j] = 1
            dfs(i, j)

print(len(house_list))
for house in sorted(house_list):
    print(house)