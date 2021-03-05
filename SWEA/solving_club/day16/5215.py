#########################
#  SWEA number 5215
#  by 김승현                
#########################

# Q. 햄버거 다이어트

def mixing(idx, mat, cal):
    global max_mat
    max_mat = max(max_mat, mat)
    if idx >= N:
        return
    for i in range(idx, N):
        if cal + ingredient[i][1] > max_cal:
            break
        mixing(i + 1, mat + ingredient[i][0], cal + ingredient[i][1])


for t in range(1, int(input())+1):
    N, max_cal = map(int, input().split())
    ingredient = []
    for n in range(N):
        ingredient.append(list(map(int, input().split())))
    ingredient = sorted(ingredient, key=lambda x: x[1])
    max_mat = 0
    mixing(0, 0, 0)
    print("#%d %d" %(t, max_mat))