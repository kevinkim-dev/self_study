def solution(m, n, board):
    def find_boom(arr):
        temp = set()
        for i in range(n-1):
            for j in range(m-2, -1, -1):
                if arr[i][j] == arr[i][j+1] == arr[i+1][j] == arr[i+1][j+1] and arr[i][j] in 'RMAFNTJC':
                    temp.add((i, j))
                    temp.add((i+1, j))
                    temp.add((i, j+1))
                    temp.add((i+1, j+1))
        return sorted(list(temp), key=lambda x: -x[1])
    answer = 0
    game = [list() for _ in range(n)]
    for i in range(n):
        for j in range(m-1, -1, -1):
            game[i].append(board[j][i])
    while True:
        for i in range(n):
            print(game[i])
        print()
        booms = find_boom(game)
        if not booms:
            break
        print(booms)
        for r, c in booms:
            game[r].pop(c)
            game[r].append('#')
            answer += 1
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))