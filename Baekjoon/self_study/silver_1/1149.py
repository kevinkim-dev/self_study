###########################
#  BaekJoon 1149번
#  by 김승현                
###########################

# Q. RGB거리

N = int(input())

dp = [[0, 0, 0]]

for i in range(N):
    rgb = list(map(int, input().split()))
    l_rgb = dp[-1]
    dp.append([rgb[0]+min(l_rgb[1], l_rgb[2]), rgb[1] + min(l_rgb[0], l_rgb[2]), rgb[2] + min(l_rgb[0], l_rgb[1])])

print(min(dp[-1]))