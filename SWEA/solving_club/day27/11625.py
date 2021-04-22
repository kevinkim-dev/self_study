#########################
#  SWEA number 11625
#  by 김승현                
#########################

# Q. BFS 코드 작성

def add_node(s, e):
    if s not in adj_list.keys():
        adj_list[s] = [e]
    else:
        if e not in adj_list[s]:
            adj_list[s].append(e)
    return


def BFS():
    while q:
        l = len(q)
        for _ in range(l):
            x = q.pop(0)
            for node in adj_list[x]:
                if node not in visited:
                    q.append(node)
                    visited.append(node)
    return


for t in range(1, int(input())+1):
    N, V = map(int, input().split())
    adj_list = dict()
    for i in range(V):
        s, e = map(int, input().split())
        add_node(s, e)
        add_node(e, s)
    q, visited = [1], [1]
    BFS()
    ans = ' '.join(list(map(str, visited)))
    print("#%d %s" %(t, ans))

# def BFS(x):
#     cnt = 0
#     for n in to_go[x]:
#         if n not in visited and n not in q:
#             q.append(n)
#             cnt += 1
#     for _ in range(cnt):
#         visited.append(q[0])
#         BFS(q.pop(0))

# t = int(input())
# N, V = map(int, input().split())
# to_go = [[] for _ in range(N+1)]
# for i in range(V):
#     s, e = map(int, input().split())
#     to_go[s].append(e)
#     to_go[e].append(s)
# q = [1]
# visited = [1]
# BFS(q.pop(0))
# print("#%d" %t, end=' ')
# print(*visited)
