###########################
#  BaekJoon 13460번
#  by 김승현                
###########################

# Q. 구슬 탈출 2

import sys
from collections import deque

input = sys.stdin.readline

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 빨간구슬
def red_turn(red, blue, dir):
    rr, rc = red
    # 뭐 만날때까지 한칸씩 이동
    while True:
        rr, rc = rr + drc[dir][0], rc + drc[dir][1]
        # 벽 만나면 그 전칸
        if board[rr][rc] == '#':
            return (rr - drc[dir][0], rc - drc[dir][1])
        # 구멍 만나면 없어짐 처리 (11, 11)은 못가는 인덱스이므로
        elif (rr, rc) == loc['O']:
            return (11, 11)
        # 파랑 만나면, 파랑 이동하고 파랑 전칸으로 가면 되므로 (0, 0)으로 false 리턴
        elif (rr, rc) == blue:
            return (0, 0)

# 파란구슬
def blue_turn(red, blue, dir):
    br, bc = blue
    # 마찬가지로 뭐 만날때까지 이동
    while True:
        br, bc = br + drc[dir][0], bc + drc[dir][1]
        # 벽이거나 빨강 만나면 그 전칸
        # 이미 빨강이 움직인 후 이므로 빨강 만나도 상관 없음
        if board[br][bc] == '#' or (br, bc) == red:
            return (br - drc[dir][0], bc - drc[dir][1])
        # 구멍 만나면 답이 아니므로 (0, 0)으로 false 리턴
        elif (br, bc) == loc['O']:
            return (0, 0)

def solution(red, blue):
    # 처음엔 네방향 다 가능하므로 last를 0~3이 아닌 -1로
    q = deque()
    q.append((red, blue, 0, -1))
    while q:
        # r은 빨간구슬 위치, b는 파란 구슬 위치
        # cnt는 움직인 횟수, last는 최근 움직인 방향의 인덱스
        r, b, cnt, last = q.popleft()
        # bfs로 10번 넘으면 나가리
        if cnt > 10:
            return -1
        # red가 (11, 11)에 있으면 답
        if r == (11, 11):
            return cnt
        # 네 방향에 대해서
        for i in range(4):
            # 방금 전과 같은 방향 혹은 반대방향이면 안해도됨
            # 단 최초 움직임이면 다 해야함
            if last in range(0, 4) and i % 2 == last % 2:
                continue
            # 빨강 먼저
            rr, rc = red_turn(r, b, i)
            # 다음 파랑
            br, bc = blue_turn((rr, rc), b, i)
            # 파랑이 구멍에 빠졌으면 더 안함
            if not br:
                continue
            # 빨강이 (0, 0)이라서 rr이 0이면 파랑이 먼저 가야하는 상황
            # 파랑 위치에서 한칸 전으로 세팅
            if not rr:
                rr, rc = br-drc[i][0], bc-drc[i][1]
            # 움직였는데 둘 다 움직이지 않았으면 버림
            if not (rr, rc) == r or not (br, bc) == b:
                q.append(((rr, rc), (br, bc), cnt + 1, i))
    return -1

R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(list(input())[:-1])

loc = dict()

# 구슬, 구멍 위치 저장하고 .으로 바꿈
for r in range(R):
    for c in range(C):
        if board[r][c] in 'BRO':
            loc[board[r][c]] = (r, c)
            board[r][c] == '.'

print(solution(loc['R'], loc['B']))