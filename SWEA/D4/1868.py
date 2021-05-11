#########################
#  SWEA number 1868
#  by 김승현                
#########################

# Q. 파핑파핑 지뢰찾기


dxy = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def check_zero(r, c):
    for d in dxy:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr <= N-1 and 0 <= nc <= N-1 and game[nr][nc] == '*':
            return False
    return True


def paping(row, col):
    q = [(row, col)]
    while q:
        r, c = q.pop()
        visited[r][c] = 1
        for d in dxy:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr <= N-1 and 0 <= nc <= N-1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                if check_zero(nr, nc):
                    q.append((nr, nc))
    return


for t in range(1, int(input())+1):
    N = int(input())
    game = [list(input()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 0
    # 첫바퀴는 0만 찾아서 조진다!
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and check_zero(i, j) and game[i][j] == '.':
                paping(i, j)
                ans += 1
    # 그리고 visit 하지 않은 남은 숫자만 눌러주면 된다!
    for i in range(N):
        for j in range(N):
            if game[i][j] == '.' and not visited[i][j]:
                ans += 1
    print("#%d %d" %(t, ans))