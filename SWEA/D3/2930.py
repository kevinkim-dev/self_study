#########################
#  SWEA number 2930
#  by 김승현                
#########################

# Q. 힙

import heapq

for t in range(1, int(input())+1):
    N = int(input())
    heap = []
    ans = []
    for _ in range(N):
        todo = input()
        if len(todo) == 1:
            if heap:
                ans.append(str(-heapq.heappop(heap)))
            else:
                ans.append('-1')
        else:
            d, x = map(int, todo.split())
            heapq.heappush(heap, -x)
    ans = ' '.join(ans)
    print("#%d %s" %(t, ans))

