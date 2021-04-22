#########################
#  SWEA number 11944
#  by 김승현                
#########################

# Q. 연산

from collections import deque

def calculate():
    cnt = 1
    while True:
        l = len(q)
        for _ in range(l):
            num = q.popleft()
            if num == M:
                return cnt-1
            for result in (num+1, num-1, num*2, num-10):
                if 1 <= result <= 1000000 and not visited[result]:
                    visited[result] = 1
                    q.append(result)
        cnt += 1


for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    min_cnt = float('inf')
    q = deque()
    q.append(N)
    visited = [0]*1000001
    print("#%d %d" %(t, calculate()))