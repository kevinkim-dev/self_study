###########################
#  BaekJoon 1932번
#  by 김승현                
###########################

# Q. 정수 삼각형

N = int(input())

triangle = []

for _ in range(N):
    triangle.append(list(map(int, input().split())))

dp = [triangle[0]]

for i in range(2, N+1):
    tmp_dp = []
    for j in range(i):
        if j == 0:
            tmp_dp.append(dp[-1][0]+triangle[i-1][0])
        elif j == i-1:
            tmp_dp.append(dp[-1][-1]+triangle[i-1][-1])
        else:
            tmp_dp.append(max(dp[-1][j-1], dp[-1][j]) + triangle[i-1][j])
    dp.append(tmp_dp)

print(max(dp[-1]))