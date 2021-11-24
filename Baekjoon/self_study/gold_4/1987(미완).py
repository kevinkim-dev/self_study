#########################
#  SWEA number 1987
#  by 김승현                
#########################

# Q. 알파벳(미완료)

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
ans = 1

q = [(0, 0, [board[0][0]], 1)]
while q:
    r, c, al_list, l = q.pop()
    ans = max(ans, l)
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in al_list:
            q.append((nr, nc, al_list + [board[nr][nc]], l+1))
            
print(ans)