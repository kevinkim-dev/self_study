#########################
#  SWEA number 1210
#  by 김승현                
#########################

# Q. ladder1

for _ in range(10):
    t = int(input())
    lad = [0]*102
    for i in range(102):
        if i == 0 or i == 101:
            lad[i] = [0]*102
        else:
            lad[i] = [0] + list(map(int, input().split())) + [0]
    # 시작점 찾기
    row = 100
    for n in range(1, 101):
        if lad[100][n] == 2:
            col = n
            break
    # direction 0 은 위로, direction 1 은 좌로, 2 는 우로    
    direction = 0
    while row > 0:
        if direction == 0:
            row -= 1
            if lad[row][col-1] == 1:
                direction = 1
            elif lad[row][col+1] == 1:
                direction = 2
        elif direction == 1:
            while lad[row][col] == 1:
                col -= 1
            col += 1
            direction = 0
        else:
            while lad[row][col] == 1:
                col += 1
            col -= 1
            direction = 0
    print("#%d %d" %(t, col-1))
