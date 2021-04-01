#########################
#  SWEA number 1873
#  by 김승현                
#########################

# Q. 상호의 배틀필드


def find_tank():
    for i in range(H):
        for j in range(W):
            if field[i][j] in tank_dir:
                return [i, j, tank_dir.index(field[i][j])]


move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
tank_dir = ['^', 'v', '<', '>']
tank_dir_alp = ['U', 'D', 'L', 'R']
for t in range(1, int(input())+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    tank = find_tank()
    N, command_str = int(input()), input()
    for n in range(N):
        command = command_str[n]
        if command in tank_dir_alp:
            tank[2] = tank_dir_alp.index(command)
            field[tank[0]][tank[1]] = tank_dir[tank[2]]
            new_r, new_c = tank[0] + move[tank[2]][0], tank[1] + move[tank[2]][1]
            if 0 <= new_r <= H-1 and 0 <= new_c <= W-1 and field[new_r][new_c] == '.':
                field[tank[0]][tank[1]] = '.'
                tank[0], tank[1] = new_r, new_c
                field[tank[0]][tank[1]] = tank_dir[tank[2]]
        else:
            distance = 1
            while True:
                shot_r, shot_c = tank[0] + distance * move[tank[2]][0], tank[1] + distance * move[tank[2]][1]
                if not 0 <= shot_r <= H-1 or not 0 <= shot_c <= W-1 or field[shot_r][shot_c] == '#':
                    break
                elif field[shot_r][shot_c] == '*':
                    field[shot_r][shot_c] = '.'
                    break
                
                else:
                    distance += 1
    print("#%d" %t, end=' ')
    for h in range(H):
        print(''.join(field[h]))


