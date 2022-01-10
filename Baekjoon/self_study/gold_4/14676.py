###########################
#  BaekJoon 14676번
#  by 김승현                
###########################

# Q. 영우는 사기꾼?

import sys

input = sys.stdin.readline

def check_build(b):
    for need in build[b]:
        if not builds[need]:
            return False
    return True


N, M, K = map(int, input().split())

build = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    build[y-1].append(x-1)

builds = [0]*N
flag = 1

for _ in range(K):
    command, b = map(int, input().split())
    b -= 1
    if command == 1:
        if not check_build(b):
            print('Lier!')
            flag = 0
            break
        builds[b] += 1
    else:
        if not builds[b]:
            print('Lier!')
            flag = 0
            break
        builds[b] -= 1 

if flag:
    print('King-God-Emperor')

