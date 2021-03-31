#########################
#  SWEA number 9663
#  by 김승현                
#########################

# Q. N-Queen (시간초과)

def Nqueen(row, visited_col, queen_list):
    global cnt
    if row == N:
        cnt += 1
        return
    for col in range(N):
        flag = 1
        if col not in visited_col:
            for queen in queen_list:
                if abs(row-queen[0]) == abs(col-queen[1]):
                    flag = 0
                    break
            if flag:
                Nqueen(row+1, visited_col + [col], queen_list + [[row, col]])
    return


N = int(input())
cnt = 0
Nqueen(0, [], [])
print(cnt)
