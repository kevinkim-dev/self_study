#########################
#  SWEA number 1987
#  by 김승현                
#########################

# Q. 알파벳(미완료)

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def find(pos, visited):
    global max_move
    if len(visited) > max_move:
        max_move = len(visited)
    r, c = pos[0], pos[1]
    for d in dxy:
        new_r, new_c = r + d[0], c + d[1]
        if 0 <= new_r <= R-1 and 0 <= new_c <= C-1 and board[new_r][new_c] not in visited:
            find((new_r, new_c), visited + list(board[new_r][new_c]))
    return


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [board[0][0]]
max_move = 0
find((0, 0), visited)
print(max_move)