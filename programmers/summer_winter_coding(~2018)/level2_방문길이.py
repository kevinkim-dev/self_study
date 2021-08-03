def solution(dirs):
    answer = 0
    lr, ud = [[0]*10 for _ in range(11)], [[0]*11 for _ in range(10)]
    now = [5, 5]
    drc = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
    for dir in dirs:
        r, c = drc[dir]
        if dir in ('L', 'R') and 0 <= now[1] + c <= 10:
            if not lr[now[0]][now[1] + (c-1)//2]:
                answer += 1
                lr[now[0]][now[1] + (c-1)//2] = 1
            now[1] += c
        elif dir in ('U', 'D') and 0 <= now[0] + r <= 10:
            if not ud[now[0] + (r-1)//2][now[1]]:
                answer += 1
                ud[now[0] + (r-1)//2][now[1]] = 1
            now[0] += r
    return answer