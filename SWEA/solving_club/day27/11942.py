#########################
#  SWEA number 11942
#  by 김승현                
#########################

# Q. 그래프에 Dijkstra 적용

def dijkstra(i, w):
    for end, weight in adj_list[i]:
        if D[end] > w + weight:
            D[end] = w + weight
            dijkstra(end, w + weight)
 
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    D = [float('inf')] * N
    adj_list = [[] for _ in range(N)]
    for _ in range(M):
        s, e, w = input().split()
        adj_list[ord(s) - 97].append((ord(e) - 97, int(w)))
    D[0] = 0
    dijkstra(0, 0)
    ans = ' '.join(map(str, D))
    print('#%d %s' % (test_case, ans))