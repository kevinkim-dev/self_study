###########################
#  BaekJoon 2010번
#  by 김승현                
###########################

# Q. 플러그

import sys

n = int(input())
plug = 0
for _ in range(n):
    plug += int(sys.stdin.readline())

print(plug -n + 1)