###########################
#  BaekJoon 21318번
#  by 김승현                
###########################

# Q. 피아노 체조

import sys

input = sys.stdin.readline

N = int(input())

akbo = list(map(int, input().split()))

mistakes = [0]*N
for i in range(0, N-1):
    mistake = 0
    if akbo[i+1] - akbo[i] < 0:
        mistake = 1
    mistakes[i+1] = mistakes[i] + mistake

Q = int(input())

ans = []

for _ in range(Q):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    ans.append(mistakes[y]-mistakes[x])

for a in ans:
    print(a)