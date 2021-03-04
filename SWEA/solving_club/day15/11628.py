#########################
#  SWEA number 11628
#  by 김승현                
#########################

# Q. 노드의 거리 코드 제출

def BFS():
    while q:
        x, l = q.pop(0)
        for n in to_go[x]:
            if n == end:
                return l+1
            elif n not in visited:
                q.append((n, l+1))
    return 0


for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    to_go = [[] for _ in range(V+1)]
    for e in range(E):
        s, e = map(int, input().split())
        to_go[s].append(e)
        to_go[e].append(s)
    start, end = map(int, input().split())
    find = 0
    q = [(start, 0)]
    visited = [start]
    print("#%d %d" %(t, BFS()))

# def BFS(x, cnt):
#     if not find:
#         for n in to_go[x]:
#             if n not in visited and n not in q:
#                 q.append(n)
#         for _ in range(cnt):
#             if find:
#                 break
#             visited.append(q[0])
#             cnt += 1
#             if q[0] == end:
#                 find = cnt
#                 return
#             BFS(q.pop(0), cnt)
#             cnt -= 1
#     return