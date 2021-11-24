#########################
#  SWEA number 17143
#  by 김승현                
#########################

# Q. 낚시왕

# 상어 잡기: 상어 무게 리턴
def fishing(c):
    for r in range(R):
        if board[r][c]:
            shark = board[r][c].pop()
            sharks[shark][-1] = 0
            return sharks[shark][4]
    return 0


# 상어 이동: r, c, s, d, z
def moving():
    for i in range(len(sharks)):
        r, c, s, d, z, live = sharks[i]
        if live:
            board[r][c].pop(0)
            if d == 1:
                if r >= s:
                    r = r - s
                elif s >= r + 1 and s <= r + R - 1:
                    d = 2
                    r = s -r
                else:
                    r = 2 * R - s + r - 2

            elif d == 2:
                if s <= R - 1 - r:
                    r = r + s
                elif s >= R - r and s <= 2 * R - r - 2:
                    d = 1
                    r = 2 * R - s - r - 2
                else:
                    r = s - 2 * R + r + 2

            elif d == 3:
                if s <= C - 1 - c:
                    c = c + s
                elif s >= C - c and s <= 2 * C - c - 2:
                    d = 4
                    c = 2 * C - s - c - 2
                else:
                    c = s - 2 * C + c + 2

            else:
                if c >= s:
                    c = c - s
                elif s >= c + 1 and s <= c + C - 1:
                    d = 3
                    c = s - c
                else:
                    c = 2 * C - s + c - 2

            if board[r][c] and board[r][c][-1] < i and (r, c) not in survive:
                survive.append((r, c))

            board[r][c].append(i)
            sharks[i] = [r, c, s, d, z, live]

    return


# 상어 먹기
def fighting():
    for r, c in survive:
        max_size = 0
        for shark in board[r][c]:
            if sharks[shark][4] > max_size:
                max_size = sharks[shark][4]
                max_num = shark

        for shark in board[r][c]:
            if shark != max_num:
                sharks[shark][-1] = 0

        board[r][c] = [max_num]
    return


# 메인
R, C, M = map(int, input().split())
# board에는 shark 번호
# sharks에는 shark 정보
board = [[[] for _ in range(C)] for _ in range(R)]
sharks = []
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    if d == 1 or d == 2:
        s %= (R - 1) * 2
    else:
        s %= (C - 1) * 2
    sharks.append([r, c, s, d, z, 1])
    board[r][c].append(i)

result = 0
for c in range(C):
    survive = []
    result += fishing(c)
    moving()
    fighting()
print(result)