#########################
#  SWEA number 9663
#  by 김승현                
#########################

# Q. N-Queen

def Nqueen(row):
    if row == N:
        return len(q)
    length = len(q)
    for _ in range(length):
        q_loc = q.pop(0)
        for col in range(N):
            flag = 1
            for r, c in q_loc:
                if c == col or abs(row-r) == abs(col-c):
                    flag = 0
                    break
            if flag:
                q.append(q_loc + [(row, col)])
    return Nqueen(row+1)


N = int(input())
q = [[(0, n)] for n in range(N)]
print(Nqueen(1))