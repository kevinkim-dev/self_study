#########################
#  SWEA number 5656
#  by 김승현                
#########################

# Q. 벽돌깨기

# 1. 전부 다 1인 col은 쏘지 않아도 됨
# 2. 깨트리고 붙이기는 replace사용
# 3. 그러려면 90도 돌려야함
# 4. 붙이는 함수와 터트리는 함수 필요
# 5. 터트리는 건 bfs 구현

# 느리네...
import copy

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def count_block(tmp_game):
    global min_block
    cnt = 0
    for r in range(W):
        cnt += H - tmp_game[r].count(0)
    min_block = min(min_block, cnt)
    return


def boom(boom_row, boom_cnt, tmp_game):
    for h in range(H):
        if tmp_game[boom_row][h] != 0:
            break
    q = [(boom_row, h)]
    visited = [(boom_row, h)]
    
    while q:
        pos = q.pop(0)
        if tmp_game[pos[0]][pos[1]] > 1:
            for d in dxy:
                for b in range(1, tmp_game[pos[0]][pos[1]]):
                    d_row = pos[0] + d[0]*b
                    d_col = pos[1] + d[1]*b
                    if 0 <= d_row <= W-1 and 0 <= d_col <= H-1 and (d_row, d_col) not in visited:
                        if tmp_game[d_row][d_col] != 0:
                            q.append((d_row, d_col))
                            visited.append((d_row, d_col))
        tmp_game[pos[0]][pos[1]] = 0
    if boom_cnt == N:
        count_block(tmp_game)
    else:
        for r in range(W):
            boom(r, boom_cnt+1, copy.deepcopy(cleanup(tmp_game)))
    return


def cleanup(tmp_game):
    for w in range(W):
        tmp_game[w] = list(map(int, ''.join(map(str, tmp_game[w])).replace('0', '').rjust(H, '0')))
    return tmp_game


for t in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(H)]
    game = list(map(list, zip(*g)))
    min_block = W*H
    for r in range(W):
        boom(r, 1, copy.deepcopy(game))
        if min_block == 0:
            break
    print("#%d %d" %(t, min_block))