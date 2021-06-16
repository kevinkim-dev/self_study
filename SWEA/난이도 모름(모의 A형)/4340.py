#########################
#  SWEA number 4340
#  by 김승현                
#########################

# Q. 파이프 연결(미완)

# def move_pipe(r, c, fr, l):
#     global min_len
#     if l >= min_len:
#         return
#     if r == N-1 and c == N-1:
#         min_len = min(min_len, l)
#         return
#     for move in pipe_move[new_map[r][c]]:
#         if fr not in move:
#             continue
#         to = sum(move) - fr
#         dr, dc = r + dxy[to][0], c + dxy[to][1]
#         if not 0 <= dr <= N-1 or not 0 <= dc <= N-1 or visited[dr][dc] or not pipe_map[dr][dc]:
#             continue
#         visited[dr][dc] = 1
#         move_pipe(dr, dc, (to + 2) % 4, l+1)
#         visited[dr][dc] = 0
#     return




# for t in range(1, int(input())+1):
#     N = int(input())
#     min_len = N**2
#     pipe_map = [list(map(int, input().split())) for _ in range(N)]
#     new_map = [[-1]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if pipe_map[i][j] in (1, 2):
#                 new_map[i][j] = 0
#             elif pipe_map[i][j] in (3, 4, 5, 6):
#                 new_map[i][j] = 1
#     visited = [[0]*N for _ in range(N)]
#     visited[0][0] = 1
#     move_pipe(0, 0, 3, 1)
#     print("#%d %d" %(t, min_len))

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

pipe_move = [((1, 3), (0, 2)), ((1, 2), (2, 3), (3, 0), (0, 1))]

def move_pipe(r, c, fr):
    if r == N-1 and c == N-1:
        return
    for move in pipe_move[new_map[r][c]]:
        if fr not in move:
            continue
        to = sum(move) - fr
        dr, dc = r + dxy[to][0], c + dxy[to][1]
        if not 0 <= dr <= N-1 or not 0 <= dc <= N-1 or visited[dr][dc] or not pipe_map[dr][dc]:
            continue
        t = (to + 2) % 4
        visited[dr][dc] = 1

        move_pipe(dr, dc, (to + 2) % 4, l+1)
        visited[dr][dc] = 0
    return


for t in range(1, int(input())+1):
    N = int(input())
    min_len = N**2
    pipe_map = [list(map(int, input().split())) for _ in range(N)]
    new_map = [[-1]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if pipe_map[i][j] in (1, 2):
                new_map[i][j] = 0
            elif pipe_map[i][j] in (3, 4, 5, 6):
                new_map[i][j] = 1
    map_move = [[[0]*4 for _ in range(N)] for _ in range(N)]
    map_move[0][0][3] = 1
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    move_pipe(0, 0, 3)
    print("#%d %d" %(t, min_len))