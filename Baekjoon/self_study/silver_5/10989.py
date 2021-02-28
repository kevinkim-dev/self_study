###########################
#  BaekJoon 10989번
#  by 김승현                
###########################

# Q. 수 정렬하기 3

import sys

N = int(input())

num_count = [0]*10000
for _ in range(N):
    num_count[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    for _ in range(num_count[i]):
        sys.stdout.write("{}\n".format(i+1))

