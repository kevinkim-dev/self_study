dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def check_dir(array, x, y, dir):
    if array[x + dx[dir]][y + dy[dir]] == 0:
        return 1
    elif array[x + dx[(dir+1)%4]][y + dy[(dir+1)%4]] == 0:
        return 2
    else:
        return -1

T = int(input())

for t in range(1, T+1):
    print("#%d" %t)
    size = int(input())
    snail = [0]*(size+2)
    for i in range(size+2):
        if i == 0 or i == size + 1:
            snail[i] = [-1]*(size+2)
        else:
            snail[i] = [-1] + [0]*size + [1]
    snail[1][1] = '1'
    count = 1
    x = 1
    y = 1
    d = 0
    while True:
        count += 1
        if check_dir(snail, x, y, d) == 1:
            x = x + dx[d]
            y = y + dy[d]
            snail[x][y] = str(count)
        elif check_dir(snail, x, y, d) == 2:
            d = (d + 1) % 4
            x = x + dx[d]
            y = y + dy[d]
            snail[x][y] = str(count)
        else:
            break
    for i in range(1, size+1):
        row = " ".join(snail[i][1:size+1])
        print(row)