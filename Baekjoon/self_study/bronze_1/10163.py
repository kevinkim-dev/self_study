###########################
#  BaekJoon 10163번
#  by 김승현                
###########################

# Q. 색종이 

N = int(input())
paper = [[-1]*101 for _ in range(101)]
size = [0]*(N+1)
for n in range(N):
    row, col, dr, dc = map(int, input().split())
    for r in range(row, row+dr):
        for c in range(col, col+dc):
            paper[r][c] = n

for i in range(101):
    for j in range(101):
        size[paper[i][j]] += 1

for i in range(N):
    print(size[i])
