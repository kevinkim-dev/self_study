#########################
#  SWEA number 14503
#  by 김승현                
#########################

# Q. 로봇 청소기

dxy = ((-1, 0), (0, 1), (1, 0), (0, -1))

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cnt = 1
room[r][c] = 2
while True:
    flag = 0
    for d_num in range(d+4, d, -1):
        di = dxy[(d_num-1) % 4]
        n_r, n_c = r + di[0], c + di[1]
        if 0 <= n_r <= N-1 and 0 <= n_c <= M-1 and room[n_r][n_c] != 1 and room[n_r][n_c] != 2:
            d = (d_num-1) % 4
            r, c = n_r, n_c
            if room[r][c] == 0:
                room[r][c] = 2
                cnt += 1
            flag = 1
            break
    if not flag:
        di = dxy[(d+2)%4]
        r, c = r + di[0], c + di[1]
        if not 0 <= r <= N-1 or not 0 <= c <= M-1 or room[r][c] == 1:
            break
print(cnt)
    
