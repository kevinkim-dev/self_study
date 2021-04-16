###########################
#  BaekJoon 11650번
#  by 김승현                
###########################

# Q. 좌표 정렬하기

import sys

dot_list = []
T = int(input())
for _ in range(T):
    dot_list.append(list(map(int, sys.stdin.readline().split())))
dot_list = sorted(dot_list, key = lambda x : (x[0], x[1]))
for t in range(T):
    print(*dot_list[t])