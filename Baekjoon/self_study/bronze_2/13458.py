###########################
#  BaekJoon 13458번
#  by 김승현                
###########################

# Q. 시험 감독

import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for a in A:
    if a > B:
        ans += 1 + math.ceil((a-B)/C)
    else:
        ans += 1

print(ans)