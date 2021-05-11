#########################
#  Programmers problem
#  Kakao internship 2021
#  by 김승현                
#########################

# Q. 2번

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(row, col, place):
    q = [(row, col, 0)]
    visited = [(row, col)]
    while q:
        r, c, n = q.pop()
        if n >= 3 or place[r][c] == 'X':
            continue
        elif place[r][c] == 'P' and n != 0:
            return False
        for d in dxy:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr <= 4 and 0 <= nc <= 4 and (nr, nc) not in visited:
                q.append((nr, nc, n+1))
                visited.append((nr, nc))
    return True


def check_place(place):
    for row in range(5):
        for col in range(5):
            if place[row][col] == 'P' and not dfs(row, col, place):
                return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check_place(place))
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))