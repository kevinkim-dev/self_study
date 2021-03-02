#########################
#  SWEA number 11606
#  by 김승현                
#########################

# Q. 미로 코드 제출

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def find_route(row, col):
    route = []
    for d in dxy:
        if miro[row+d[0]][col+d[1]] == '0' or miro[row+d[0]][col+d[1]] == '2':
            route.append(d)
        elif miro[row+d[0]][col+d[1]] == '3':
            route.append((0,0))
            break
    return route

for t in range(1, int(input())+1):
    N = int(input())
    miro = [0]*(N+2)
    for i in range(N+2):
        if i == 0 or i == N+1:
            miro[i] = ['1']*(N+2)
        else: 
            miro[i] = ['1'] + list(input()) + ['1']
    # 시작점 찾기 
    for r in range(1, N+1):
        if '2' in miro[r]:
            start = r, miro[r].index('2')
        if '3' in miro[r]:
            end = r, miro[r].index('3')
    row, col = start[0], start[1]
    stack = []
    while True:
        route = find_route(row, col)
        if not route:
            if stack:
                miro[row][col] = '1'
                ret = stack.pop()
                row = ret[0]
                col = ret[1]
            else:
                print("#%d 0" %t)
                break
        elif route[-1] == (0,0):
            print("#%d 1" %t)
            break
        elif len(route) >= 3 or (len(route) == 2 and (row, col) == start):
            for _ in range(len(route)+ ((row, col) == start) -2):
                stack.append((row, col))
            row += route[0][0]
            col += route[0][1]
        elif len(route) == 2 or len(route) == 1:
            miro[row][col] = '1'
            row += route[0][0]
            col += route[0][1]
        
        # for i in range(N+2):
        #     print(*miro[i])
        # print(row, col)