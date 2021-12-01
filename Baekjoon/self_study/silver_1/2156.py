###########################
#  BaekJoon 2156번
#  by 김승현                
###########################

# Q. 포도주 시식

N = int(input())

wine_list = []

for _ in range(N):
    wine_list.append(int(input()))

dp = [[0, 0], [0, 0], [wine_list[0], 0]]

ans = wine_list[0]

for i in range(1, N):
    pp = max(dp[-2][0], dp[-2][1], dp[-3][0], dp[-3][1]) + wine_list[i]
    p = dp[-1][0] + wine_list[i]
    dp.append([pp, p])
    ans = max(ans, p, pp)

print(ans)