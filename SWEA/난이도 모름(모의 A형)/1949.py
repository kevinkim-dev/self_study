#########################
#  SWEA number 1949
#  by 김승현                
#########################

# Q. 등산로 조성

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def find_route(pos_height, pos, visited, cnt, flag):
    global max_cnt
    # 네 방향에 대해서
    for d in dxy:
        row = pos[0] + d[0]
        col = pos[1] + d[1]
        # 갈 수 있는 곳이면
        if 0 <= row <= N-1 and 0 <= col <= N-1 and [row, col] not in visited:
            # 그냥 갈 수 있으면 간다
            if pos_height > mountain[row][col]:
                find_route(mountain[row][col], [row, col], visited + [[row, col]], cnt+1, flag)
            # 깎아서 갈 수 있으면 깎고 간다
            elif pos_height <= mountain[row][col] and flag and k > mountain[row][col]-mountain[pos[0]][pos[1]]:
                find_route(pos_height-1, [row, col], visited + [[row, col]], cnt+1, flag-1)
            else:
                max_cnt = max(max_cnt, cnt)

    return

def find_top():
    top = 0
    top_loc = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > top:
                top = mountain[i][j]
                top_loc = [[i, j]]
            elif mountain[i][j] == top:
                top_loc.append([i, j])
    return top_loc


for t in range(1, int(input())+1):
    N, k = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    top_loc = find_top()
    for top in top_loc:
        visited = [top]
        find_route(mountain[top[0]][top[1]], top, visited, 1, 1)
    print("#%d %d" %(t, max_cnt))

                # if cnt > max_cnt:
                #     max_cnt = cnt
                #     print(visited)